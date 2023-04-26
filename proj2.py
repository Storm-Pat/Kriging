import os
import glob
import pandas as pd


def tolatlon(df):
    idx = pd.IndexSlice
    long = df.iloc[idx[:, 0]].astype(float)
    lat = df.iloc[idx[:, 1]].astype(float)
    df1 = df.iloc[idx[:, 2]].astype(float)
    # settings the depth values negative
    dfneg = -1 * df1
    fulldf = [long, lat, dfneg]
    # removing positive values
    # df = dfneg >= 0.0
    # print(df)
    # print(type(df))
    return long, lat, dfneg, fulldf

def createdataframe(latitude, longitude, depth):
    df = pd.DataFrame({'Latitude': latitude, 'Longitude': longitude, 'Depth_m': depth}).astype("float64")
    return df