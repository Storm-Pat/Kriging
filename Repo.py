import geopandas
import os


def repo(long, lat, df):
    home_dir = os.path.expanduser('~')
    path1 = 'Documents'
    path2 = os.path.join(home_dir, path1)
    path3 = 'Field-Interp-Tool'
    path4 = os.path.join(path2, path3)
    path5 = 'Input_CSV'
    output = 'output_files'
    path6 = os.path.join(path4, path5)
    os.path.exists(path6)
    path8 = os.path.join(path4, output)
    path9 = os.path.join(path8, "cookie-cutter.shp")
    if os.path.exists(path6):
        # changing coords, changes the projection too
        columns = {'long': long, 'lat': lat}
        shapefull = geopandas.GeoDataFrame(columns, geometry=geopandas.points_from_xy(long, lat, df), crs="EPSG:4326")
        # reading it back out to a file under the cookie cutters, separate from the shapefiles
        # grabbing the min and maxes
        extrema = shapefull.bounds
        lon_min = (extrema['minx'].min())
        lon_max = (extrema['maxx'].max())
        lat_min = (extrema['miny'].min())
        lat_max = (extrema['maxy'].max())
        shapefull.to_file(path9, driver="ESRI Shapefile")
        return shapefull, lat_max, lat_min, lon_max, lon_min
