#!./usr/bin/env python
# I refuse to use oop for this project
import shutil
import os
import pandas as pd
import Kriging
import Write_Shape
import Write_Tiff
import Repo
import Chauv
import Clip
import CV
import proj
import numpy as np
import LargeInterp


# main function
def dropSEQ(CSV, SHP, ML, lags_true, EXV, dropdown, dirtval):
    print(CSV)
    print(SHP)
    print(ML)
    print(lags_true)
    print(EXV)
    print(dropdown)
    print(dirtval)
    LargeInterp.csvfile(CSV)
    # create a dropping sequence that allows the gui to send the values to the back end
    home_dir = os.path.expanduser('~')
    # "naming" directories to store i/o operations
    directory1 = 'Input_CSV'
    directory2 = 'Input_SHP'
    directory3 = 'output_files'
    # parent directory
    parent_directory = 'Field-Interp-Tool'
    path0 = os.path.join(home_dir, 'Documents')
    path1 = os.path.join(path0, parent_directory)
    path2 = os.path.join(path1, directory1)  # CSV
    path3 = os.path.join(path1, directory2)  # SHP
    path4 = os.path.join(path1, directory3)  # output files
    if not os.path.exists(path2):
        os.mkdir(path2)
    else:
        path2 = path2
        dir1 = os.listdir(path2)
        if len(dir1) != 0:
            shutil.rmtree(path2)
            os.mkdir(path2)
            # deletes the contents of the input files if there are any present
    if not os.path.exists(path3):
        os.mkdir(path3)
    else:
        path3 = path3
        dir2 = os.listdir(path3)
        if len(dir2) != 0:
            shutil.rmtree(path3)
            os.mkdir(path3)
            # deletes the contents of the input files if there are any present
    if not os.path.exists(path4):
        os.mkdir(path4)
    else:
        path4 = path4

    # actually creating and appending directories
    # call the GUI

    # really the main while loop where the magic happens after initializing everything
    shutil.copy(CSV, path2)
    shutil.copy(SHP, path3)
    # copying data over to program directories (its more fun this way, trust me)
    while True:
        # concatenating and labeling the data
        long, lat, df, fulldf = proj.tolatlon()
        # for the large datasets that need to be interpolated
        if len(df) > 20000:
            idx = pd.IndexSlice
            zi, yi, xi = np.histogram2d(df.iloc[idx[:, 1]], df.iloc[idx[:, 0]], bins=(140, 140),
                                        weights=df.iloc[idx[:, 2]], normed=False)
            counts, _, _ = np.histogram2d(df.iloc[idx[:, 1]], df.iloc[idx[:, 0]], bins=(140, 140))
            zi = zi / counts
            # correcting for the difference in zi and the axis
            xi = np.linspace(xi.min(), xi.max(), len(zi), zi.shape[0], dtype="float64")
            yi = np.linspace(yi.min(), yi.max(), len(zi), zi.shape[1], dtype="float64")
            zi = np.ma.masked_invalid(zi)
            xx, yy = np.meshgrid(xi, yi)
            # get valid vals
            x1 = xx[~zi.mask]
            y1 = yy[~zi.mask]
            z1 = zi[~zi.mask] * -1
            df = pd.DataFrame({'Longitude': y1, 'Latitude': x1, 'Depth_m': z1}).astype("float64")
        # cleaning algorithm,returns chosen dataframe
        df = Chauv.chauv(df, dirtval)
        # re-projecting the shapefile
        shape, lat_max, lat_min, lon_max, lon_min = Repo.repo(long, lat, df, CSV)
        # writing shape file
        Write_Shape.write_file(long, lat, df)
        # searching for best parameters to try
        while True:
            if ML:
                # calling our wonderful ML function
                CV.cv(df)
                break
            elif not ML:
                break
                # ML is a boolean value from the GUI
        # prompting user to run kriging type
        # nlags checking
        while True:
            intlag = 0
            if lags_true == "6":
                intlag = 6
            elif lags_true == "8":
                intlag = 8
            elif lags_true == "10":
                intlag = 10
            elif lags_true == "15":
                intlag = 15
            elif lags_true == "20":
                intlag = 20
            else:
                intlag = 20
                # if the value is somehow undetermined, intlag (number of lags) will automatically be set at 20
            nlags = intlag
            try:
                nlags = intlag
                break
                # since the GUI returns a string, setting a new variable to a value will avoid a string to int cast
            except:
                continue
                # grabs the value from the gui received for exact values
        exact = EXV
        # START OF KRIGING #
        # we pass shape to mask the interpolation
        # Also going to error check in case of singular matrix or overload
        krig_type = dropdown
        z, ss, gridx, gridy = Kriging.kriging(fulldf, shape, lat_min, lat_max, lon_min, lon_max, nlags, krig_type, exact)
        # writing the tiff function, the grid is passed to define resolution, data frame defines domain and range,
        # z for values
        Write_Tiff.write_file(z, ss, gridx, gridy, lat_min, lat_max, lon_min, lon_max)

        # clipping the tif here, using the cookie cutter and outputted tiff underwrite tiff function.
        Clip.clip(SHP)
        return
