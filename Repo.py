import os
import geopandas as gpd
import glob


def repo():
    # grabbing the shp file automatically
    dir = 'kriging/input/'
    # TODO need to replace this whole thing with the GUI, it automatically validates the file type
    # TODO this will reduce complexity of this file and reduce my migraine
    while True:
        try:
            for f in os.listdir(dir):
                if f.endswith('.csv' or '.shp'):
                    shape = gpd.read_file(dir + f)
                    # validating the .shp files
                    break
                else:
                    print("I built it wrong *cri*")
            break
        except:
            print("Shape file loading error, make sure correct files are in the directory")
            quit()
    # changing coords, changes the projection too
    shapefull = shape.set_crs(epsg=4326)
    # reading it back out to a file under the cookie cutters, separate from the og shapefiles
    shapefull.to_file(driver='ESRI Shapefile', filename=f"cookie_cutters")
    # Shit becomes shape again in main lol
    # grabbing the min and maxes
    extrema = shapefull.bounds
    lon_min = (extrema['minx'])
    lon_max = (extrema['maxx'])
    lat_min = (extrema['miny'])
    lat_max = (extrema['maxy'])
    return shapefull, lat_max, lat_min, lon_max, lon_min
