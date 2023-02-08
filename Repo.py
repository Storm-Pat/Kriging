import geopandas as gpd
import os


def repo(CSV):
    # grabbing the shp file automatically

    # THIS ACTION HAS SAVED MY SANITY #
    # dir = 'kriging/input/'
    # while True:
    #     try:
    #         for f in os.listdir(dir):
    #             if f.endswith('.csv'):
    #                 shape = gpd.read_file(dir + f)
    #                 # validating the .shp files
    #                 break
    #             else:
    #                 print("I built it wrong *cri*")
    #         break
    #     except:
    #         print("Shape file loading error, make sure correct files are in the directory")
    #         quit()
    # DO NOT USE THIS BLOCK OF CODE PLEASE #
    home_dir = os.path.expanduser('~')
    path1 = 'Documents'
    path2 = os.path.join(home_dir, path1)
    path3 = 'Field-Interp-Tool'
    path4 = os.path.join(path2, path3)
    path5 = 'Input_CSV'
    path6 = os.path.join(path4, path5)
    os.path.exists(path6)
    path7 = os.path.join(path6, CSV)
    if os.path.exists(path6):
        shape = gpd.read_file(path7)
        # changing coords, changes the projection too
        shapefull = shape.set_crs(epsg=4326)
        # reading it back out to a file under the cookie cutters, separate from the og shapefiles
        shapefull.to_file(driver='ESRI Shapefile', filename="cookie_cutters")
        # grabbing the min and maxes
        extrema = shapefull.bounds
        lon_min = (extrema['minx'])
        lon_max = (extrema['maxx'])
        lat_min = (extrema['miny'])
        lat_max = (extrema['maxy'])
        return shapefull, lat_max, lat_min, lon_max, lon_min
