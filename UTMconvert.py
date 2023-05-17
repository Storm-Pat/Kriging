import utm
import pandas as pd

def utmconverter(letter, number, fulldf):
    idx = pd.IndexSlice
    if type(fulldf) == list:
        long = fulldf[0]
        lat = fulldf[1]
        depth = fulldf[2]
    else:
        long = fulldf.iloc[idx[:, 0]]
        lat = fulldf.iloc[idx[:, 1]]
        depth = fulldf.iloc[idx[:, 2]]
    dftolatlon = utm.to_latlon(long, lat, number, letter)
    df = pd.DataFrame({'Latitude': dftolatlon[0], 'Longitude': dftolatlon[1], 'Depth_m': depth}).astype("float64")
    latitude = dftolatlon[0]
    longitude = dftolatlon[1]
    depthvalue = depth
    return latitude, longitude, depthvalue, df

def returnutm(letter, number, lat, long):
    dftoutm = utm.from_latlon(lat, long, number, letter)
    latitude = dftoutm[0]
    longitude = dftoutm[1]
    return latitude, longitude