import geopandas as gpd
import GUI_test


def repo():
    # call the GUI
    CSV, SHP, LONG_MIN, LONG_MAX, LAT_MIN, LAT_MAX, dropdown, ML, EXV, WHEY, lags_true = GUI_test.maingui()
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

    shape = gpd.read_file(CSV)
    # changing coords, changes the projection too
    shapefull = shape.set_crs(epsg=4326)
    # reading it back out to a file under the cookie cutters, separate from the og shapefiles
    shapefull.to_file(driver='ESRI Shapefile', filename="cookie_cutters")
    # Shit becomes shape again in main lol
    # grabbing the min and maxes
    extrema = shapefull.bounds
    lon_min = (extrema['minx'])
    lon_max = (extrema['maxx'])
    lat_min = (extrema['miny'])
    lat_max = (extrema['maxy'])
    return shapefull, lat_max, lat_min, lon_max, lon_min
