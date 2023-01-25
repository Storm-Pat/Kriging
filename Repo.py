import geopandas as gpd
import Main


def repo():
    # call the GUI
    csv_gui = None
    shp_gui = None
    mach_learn = None
    lags_true_gui = None
    exval = None
    krigtype = None
    dirt = None

    CSV, SHP, ML, lags_true, EXV, dropdown, dirtval = Main.guidrop(csv_gui, shp_gui, mach_learn, lags_true_gui, exval,
                                                              krigtype, dirt)
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
    # grabbing the min and maxes
    extrema = shapefull.bounds
    lon_min = (extrema['minx'])
    lon_max = (extrema['maxx'])
    lat_min = (extrema['miny'])
    lat_max = (extrema['maxy'])
    return shapefull, lat_max, lat_min, lon_max, lon_min
