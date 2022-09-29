import geopandas as gpd
def repo():
    shape = gpd.read_file('testing data/Perserved OG shapefiles/I96Billwood_GrandRiverMask.shp')
    #changing coords, idk why I named this shit, kinda funny actually, anyway this changes the projection too
    shit = shape.to_crs(epsg=4326)
    #reading it back out to a file under the cookie cutters, seperate from the og shapefiles
    shit.to_file(driver='ESRI Shapefile',filename=f"/home/pabritt/Krig/cookie_cutters")
    #Shit becomes shape again in main lol
    return shit
