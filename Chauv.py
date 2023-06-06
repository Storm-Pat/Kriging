import pandas as pd
import scipy as sp
import numpy as np
import os
import UTMconvert

home_dir = os.path.expanduser('~')
parent_directory = 'Field-Interp-Tool'
directory1 = 'output_files'
path0 = os.path.join(home_dir, 'Documents')
path1 = os.path.join(path0, parent_directory)
path2 = os.path.join(path1, directory1)


def chauv(depth, dirtval, long, lat, seaval, utmval, utmletterval, utmnumberval):
    if dirtval is True:
        iternum = 0
        idx = pd.IndexSlice
        # defining boundary p value
        maxdev = 1 / (2 * len(depth))
        # initializing what will be clean dataframe
        # dirty array
        dirty = []
        # mean value
        mean = depth.mean()
        # standard deviation
        sigma = depth.std()
        # z score function
        z = (lambda a: abs(a - mean) / sigma)
        # calculation to find the depth as mean sea level in feet
        # meters to feet: 1 meter = 3.28084 feet
        # creates a function with an anonymous variable (a) that will be filled in the for loop
        msl = seaval + depth
        # creating a dataframe that can be used for interpolation
        dataframe = pd.DataFrame({'X': lat, 'Y': long, 'Z_hae': msl}).astype("float64")
        # creating a dataframe
        for i in depth:
            iternum = iternum + 1
            # computing z score
            zscore = z(i)
            # applying z score to 1-erf to produce a probability
            deviation = (sp.special.erfc(zscore))
            # checking the probability function output against the boundary
            if i > 0:
                iternum = iternum - 1
                dirty.append(i)
                dataframe.drop(dataframe.index[iternum], inplace=True)
            if deviation < maxdev:
                iternum = iternum - 1
                dirty.append(i)
                dataframe.drop(dataframe.index[iternum], inplace=True)
            else:
                continue
        if type(dataframe) == list:
            latdf = dataframe[0]
            longdf = dataframe[1]
            depthdf = dataframe[2]
        else:
            latdf = dataframe.iloc[idx[:, 0]]
            longdf = dataframe.iloc[idx[:, 1]]
            depthdf = dataframe.iloc[idx[:, 2]]
        path3 = os.path.join(path2, "clean_data.csv")
        iternumtwo = 0
        if utmval is True:
            TRUElat, TRUElong, depthvalue, df = UTMconvert.utmconverter(utmletterval, utmnumberval, dataframe)
            # creating a csv with coordinates in both WGS84 EPSG:4326 and UTM as well as with depth and HAE
            dataframetwo = pd.DataFrame(
                {'Latitude': TRUElat, 'Longitude': TRUElong, 'Depth_m': depth,
                 'Alt_hae_m': msl, 'X_Northing': longdf, 'Y_Easting': latdf}).astype("float64")
            for i in depth:
                iternumtwo = iternumtwo + 1
                zscore = z(i)
                deviation = (sp.special.erfc(zscore))
                if i > 0:
                    iternumtwo = iternumtwo - 1
                    dirty.append(i)
                    dataframetwo.drop(dataframetwo.index[iternumtwo], inplace=True)
                if deviation < maxdev:
                    iternumtwo = iternumtwo - 1
                    dirty.append(i)
                    dataframetwo.drop(dataframetwo.index[iternumtwo], inplace=True)
                else:
                    continue
            dataframetwo.to_csv(path3)
        else:
            longdf, latdf = UTMconvert.backtoutm(utmletterval, utmnumberval, dataframe)
            dataframetwo = pd.DataFrame(
                {'Latitude': lat, 'Longitude': long, 'Depth_m': depth,
                 'Alt_hae_m': msl, 'X_Northing': longdf, 'Y_Easting': latdf}).astype("float64")
            for i in depth:
                iternumtwo = iternumtwo + 1
                zscore = z(i)
                deviation = (sp.special.erfc(zscore))
                if i > 0:
                    iternumtwo = iternumtwo - 1
                    dirty.append(i)
                    dataframetwo.drop(dataframetwo.index[iternumtwo], inplace=True)
                if deviation < maxdev:
                    iternumtwo = iternumtwo - 1
                    dirty.append(i)
                    dataframetwo.drop(dataframetwo.index[iternumtwo], inplace=True)
                else:
                    continue
            dataframetwo.to_csv(path3)

        print(dirty)
        return dataframe

    elif dirtval is False:
        # if the error is left within the csv
        path3 = os.path.join(path2, "full_data.csv")
        idx = pd.IndexSlice
        dataframe = pd.DataFrame({'X': lat, 'Y': long, 'Z_hae': depth}).astype("float64")
        if type(dataframe) == list:
            latdf = dataframe[0]
            longdf = dataframe[1]
            depthdf = dataframe[2]
        else:
            latdf = dataframe.iloc[idx[:, 0]]
            longdf = dataframe.iloc[idx[:, 1]]
            depthdf = dataframe.iloc[idx[:, 2]]
        msl = seaval + depthdf
        if utmval is True:
            TRUElat, TRUElong, depthvalue, df = UTMconvert.utmconverter(utmletterval, utmnumberval, dataframe)
            dataframeforschoh = pd.DataFrame(
                {'Latitude': TRUElat, 'Longitude': TRUElong, 'Depth_m': depthdf,
                 'Alt_hae_m': msl, 'X_Northing': longdf, 'Y_Easting': latdf}).astype("float64")
            dataframeforschoh.to_csv(path3)
        else:
            longdf, latdf = UTMconvert.backtoutm(utmletterval, utmnumberval, dataframe)
            dataframeforschoh = pd.DataFrame(
                {'Latitude': lat, 'Longitude': long, 'Depth_m': depth,
                 'Alt_hae_m': msl, 'X_Northing': longdf, 'Y_Easting': latdf}).astype("float64")
            dataframeforschoh.to_csv(path3)
        return dataframe
