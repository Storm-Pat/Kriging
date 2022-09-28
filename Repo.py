import geopandas as gpd
def repo():
    shape = gpd.read_file('/home/pabritt/Krig/testing data/preserved2/gallup_boundary_line.shp')
    #changing coords, reeeeeeeee, idk why I named this shit, kinda funny actually, anyway this changes the projection too
    shit = shape.to_crs(epsg=4326)
    #reading it back out to a file under the cookie cutters, seperate from the og shapefiles
    shit.to_file(driver='ESRI Shapefile',filename = f"/home/pabritt/Krig/cookie_cutters/cookiecutters.shp")
    #Shit becomes shape again in main lol
    return shit