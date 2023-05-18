import os
import pandas as pd
import geopandas

home_dir = os.path.expanduser('~')
parent_directory = 'Field-Interp-Tool'
directory1 = 'output_files'
path0 = os.path.join(home_dir, 'Documents')
path1 = os.path.join(path0, parent_directory)
path2 = os.path.join(path1, directory1)
path3 = os.path.join(path2, "output.csv")
path4 = os.path.join(path2, "Complete-shape.shp")


# defining the paths


def write_file(long, lat, df):
    columns = {'lat': lat, 'long': long, 'depth(m)': df}
    # creating a csv with corrected negative depth values
    data = pd.DataFrame(columns)
    data.to_csv(path3)
    # writing the dataframe out to csv file
    geodata = geopandas.GeoDataFrame(geometry=geopandas.points_from_xy(lat, long, df))
    # inputting the dataframe into a geodataframe
    geodata.to_file(path4, driver='ESRI Shapefile', encoding='utf-8', crs='EPSG:4326', engine="fiona")
    # inserting into a point shapefile with base coordinate system
