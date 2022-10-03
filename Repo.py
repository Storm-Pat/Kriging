import os
import geopandas as gpd
import glob
def repo():
    #grabbing the shp file automatically
    dir = 'input/'
    while True:
        try:
            for f in os.listdir(dir):
                if f.endswith('.shp'):
                    shape = gpd.read_file(dir + f)
                    break
            break
        except:
            print("Shape file loading error, make sure correct files are in the directory")
            quit()
    #changing coords, idk why I named this shit, kinda funny actually, anyway this changes the projection too
    shit = shape.to_crs(epsg=4326)
    #reading it back out to a file under the cookie cutters, seperate from the og shapefiles
    shit.to_file(driver='ESRI Shapefile',filename=f"/home/pabritt/Krig/cookie_cutters")
    #Shit becomes shape again in main lol
    #grabbing the min and maxes
    extrema=shit.bounds
    lon_min=float(extrema['minx'])
    lon_max=float(extrema['maxx'])
    lat_min=float(extrema['miny'])
    lat_max=float(extrema['maxy'])
    return shit,lat_max,lat_min,lon_max,lon_min
