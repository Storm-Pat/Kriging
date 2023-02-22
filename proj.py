import os
import glob
import pandas as pd


# Function to handle Iver 3 data
def tolatlon():
    # since iver3 datasets tend to be very large, we are taking all the data and putting it over a sparse matrix
    # we then take the average of that grid and put it into a larger grid that has kriging applied to it
    # this will significantly reduce computational time
    home_dir = os.path.expanduser('~')
    parent_directory = 'Field-Interp-Tool'
    directory1 = 'Input_CSV'
    path0 = os.path.join(home_dir, 'Documents')
    path1 = os.path.join(path0, parent_directory)
    path2 = os.path.join(path1, directory1)
    # introducing the path where the input files are being stored
    CSV = os.listdir(path2)
    for x in CSV:
        # set up for list of files (for later in development)
        path3 = os.path.join(path2, x)
        # checking the path
        # creating a list of all the files in the csv director
        df = pd.concat([pd.read_csv(path3, sep=',', header=None)])
        idx = pd.IndexSlice
        long = df.iloc[idx[:, 0]].astype(float)
        lat = df.iloc[idx[:, 1]].astype(float)
        df = df.iloc[idx[:, 2]].astype(float)
        # settings the depth values negative
        df1 = -1 * df
        # removing positive values
        # df = df1 >= 0.0
        # print(df)
        # print(type(df))
        return long, lat, df1
