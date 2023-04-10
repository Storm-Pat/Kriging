import os
import glob
import pandas as pd


def tolatlon(df):
    print("this is 1")
    print(len(df))
    idx = pd.IndexSlice
    long = df.iloc[idx[:, 0]].astype(float)
    lat = df.iloc[idx[:, 1]].astype(float)
    df1 = df.iloc[idx[:, 2]].astype(float)
    # settings the depth values negative
    print("this is 2")
    print(len(df1))
    dfneg = -1 * df1
    fulldf = [long, lat, dfneg]
    # removing positive values
    # df = dfneg >= 0.0
    # print(df)
    # print(type(df))
    print("this is 3")
    print(len(dfneg))
    return long, lat, dfneg, fulldf
