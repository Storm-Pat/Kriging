import os
import glob
import pandas as pd


def tolatlon():
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
        df = df.drop(df.index[0])
        # removes the first row to remove possible strings
        idx = pd.IndexSlice
        long = df.iloc[idx[:, 0]].astype(float)
        lat = df.iloc[idx[:, 1]].astype(float)
        df = df.iloc[idx[:, 2]].astype(float)
        # settings the depth values negative
        df1 = -1 * df
        fulldf = [long, lat, df1]
        # removing positive values
        # df = df1 >= 0.0
        lengthfile = (len(df1))
        return long, lat, df1, fulldf, lengthfile
