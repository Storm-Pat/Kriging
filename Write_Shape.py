import fiona
import os

home_dir = os.path.expanduser('~')
parent_directory = 'Field-Interp-Tool'
directory1 = 'output_files'
path0 = os.path.join(home_dir, 'Documents')
path1 = os.path.join(path0, parent_directory)
path2 = os.path.join(path1, directory1)
path3 = os.path.join(path2, "output.shp")
# reading in function, takes file as an argument
def write_file(df):
    # setting up fiona schema
    schema = {'geometry': 'Point', 'properties': [('Depth_m', 'float')]}
    # creating a fiona object
    shape = fiona.open(path3, mode='w', driver='ESRI Shapefile', schema=schema, crs='WGS84')

    # creating points list
    for i, j in df[[' Longitude', ' Latitude']].iterrows():
        # TODO none of these are "in the index". should be first thing fixed, we are close to a solution.
        rowDict = {'geometry': {'type': 'Point', 'coordinates': (j.Longitude, j.Latitude)},
                   "properties": {'Depth_m': df[i, 2]}}
        shape.write(rowDict)
    # writing and closing the file
    shape.close()
