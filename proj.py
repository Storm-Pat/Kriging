import os
import pandas as pd


def tolatlon(path2):
    # introducing the path where the input files are being stored
    CSV = os.listdir(path2)
    for x in CSV:
        # set up for list of files (for later in development(possibly))
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
        depth = -1 * df
        # building the dataframe
        fulldf = [long, lat, depth]
        # getting the length of the dataframe
        lengthfile = (len(depth))
        # returning the long, lat, depth, dataframe, and length of the file
        return long, lat, depth, fulldf, lengthfile
