import utm
import pandas as pd

def utmconverter(letter, number, fulldf):
    # for if it's either a list or dataframe
    idx = pd.IndexSlice
    if type(fulldf) == list:
        lat = fulldf[0]
        long = fulldf[1]
        depth = fulldf[2]
    else:
        lat = fulldf.iloc[idx[:, 0]]
        long = fulldf.iloc[idx[:, 1]]
        depth = fulldf.iloc[idx[:, 2]]
    # converting from UTM to WGS84 EPSG:4326 in order to perform interpolation
    dftolatlon = utm.to_latlon(lat, long, number, letter)
    df = pd.DataFrame({'Latitude': dftolatlon[0], 'Longitude': dftolatlon[1], 'Depth_m': depth}).astype("float64")
    latitude = dftolatlon[0]
    longitude = dftolatlon[1]
    depthvalue = dftolatlon[2]
    # returning both individual columns and the whole dataframe
    return latitude, longitude, depthvalue, df

def backtoutm(letter, number, fulldf):
    # converting from WGS84 EPSG:4326 to UTM
    idx = pd.IndexSlice
    if type(fulldf) == list:
        lat = fulldf[0]
        long = fulldf[1]
        depth = fulldf[2]
    else:
        lat = fulldf.iloc[idx[:, 0]]
        long = fulldf.iloc[idx[:, 1]]
        depth = fulldf.iloc[idx[:, 2]]
    utmdf = utm.from_latlon(lat, long, number, letter)
    # splitting the dataframe into 2 (easting/northing) then returning the values
    easting = utmdf[0]
    northing = utmdf[1]
    return northing, easting
