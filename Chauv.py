import pandas as pd
import scipy as sp
import os
import UTMconvert

home_dir = os.path.expanduser('~')
parent_directory = 'Field-Interp-Tool'
directory1 = 'output_files'
path0 = os.path.join(home_dir, 'Documents')
path1 = os.path.join(path0, parent_directory)
path2 = os.path.join(path1, directory1)


def chauv(depth, dirtval, long, lat, seaval, utmletterval, utmnumberval):
    if dirtval is True:
        iternum = 0
        idx = pd.IndexSlice
        # defining boundary p value
        maxdev = 1 / (2 * len(depth))
        # initializing what will be clean data_frame
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
        msl = seaval + depth
        # creates a function with an anonymous variable (a) that will be filled in the for loop
        bathy = "MTRI_Bathyboat"
        dataframe = pd.DataFrame({'X': long, 'Y': lat, 'Z_hae': msl}).astype("float64")
        # creating a dataframe
        for i in depth:
            iternum = iternum + 1
            print(iternum)
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
        idx = pd.IndexSlice
        if type(dataframe) == list:
            latdf = dataframe[0]
            longdf = dataframe[1]
            depthdf = dataframe[2]
        else:
            latdf = dataframe.iloc[idx[:, 0]]
            longdf = dataframe.iloc[idx[:, 1]]
            depthdf = dataframe.iloc[idx[:, 2]]
        path3 = os.path.join(path2, "clean_data.csv")
        TRUElat, TRUElong, depthvalue, df = UTMconvert.utmconverter(utmletterval, utmnumberval, dataframe)
        dataframeforschoh = pd.DataFrame({'Latitude': TRUElat, 'Longitude': TRUElong, 'Depth_m': depthdf,
                                          'Alt_hae_m': msl, 'Northing': longdf, 'Easting': latdf}).astype("float64")
        dataframeforschoh.to_csv(path3)
        print(dirty)
        return dataframe

    elif dirtval is False:
        # if the error is left within the csv
        msl = seaval + depth
        dataframe = pd.DataFrame({'Longitude': long, 'Latitude': lat, 'Z_hae': msl}).astype("float64")
        path3 = os.path.join(path2, "full_data.csv")
        dataframe.to_csv(path3)
        return dataframe
