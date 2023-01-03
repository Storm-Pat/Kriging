#!./usr/bin/env python
# I refuse to use oop for this project
import os
import shutil
import pandas as pd
# import Kriging
import Write_Shape
# import Write_Tiff
# import Clip
import Repo
import Chauv
# import Switch
import CV
import proj
import GUI_test
import numpy as np

# main function
if __name__ == '__main__':
    CSV, SHP, LONG_MIN, LONG_MAX, LAT_MIN, LAT_MAX, dropdown, ML, EXV, WHEY, lags_true = GUI_test.maingui()
    # TODO implement all GUI (link it to back end code)
    # truncating the cookie cutters, shapefiles, and outputtiff folder here
    # starting with the cookie cutters
    shutil.rmtree('cookie_cutters')
    os.mkdir('cookie_cutters')
    # same but with point shapefiles
    shutil.rmtree('Kriging/Outputs')
    os.mkdir('Kriging/Outputs')
    # really the main while loop where the magic happens after initializing everything
    while True:
        # concatenating and labeling the data
        df = proj.tolatlon()
        # for the large datasets that need to be interpolated
        if len(df) > 20000:
            zi, yi, xi = np.histogram2d(df.iloc[:, 1], df.iloc[:, 0], bins=(140, 140), weights=df.iloc[:, 2],
                                        normed=False)
            counts, _, _ = np.histogram2d(df.iloc[:, 1], df.iloc[:, 0], bins=(140, 140))
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
            print("CSV size too large, new DF: \n", df)
        # cleaning algorithm,returns chosen dataframe
        df = Chauv.chauv(df)
        # re-projecting the shapefile
        shape, lat_max, lat_min, lon_max, lon_min = Repo.repo()
        # writing shape file
        Write_Shape.write_file(df)
        # UGLY ASS YANDERE DEV USER INPUT BOILERPLATE
        # If only python 3.9 supported using match as a switch statement
        # searching for best parameters to try
        while True:
            if ML == True:
                # calling our wonderful ML function
                CV.cv(df)
                break
            elif ML == False:
                break
            else:
                print("Enter a valid input")
        # prompting user to run kriging type
        krig_type = dropdown
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
            nlags = intlag
            try:
                nlags = intlag
                break
            except:
                continue
        # prompting the user to select the whether to use exact values or not
        while True:
            exact = EXV

        # START OF KRIGING #
        # we pass shape to mask the interpolation
        # Also going to error check in case of singular matrix or overload
        z, ss, gridx, gridy = Kriging.kriging(df, shape, lat_min, lat_max, lon_min, lon_max, nlags, krig_type, exact)
        # writing the tiff function, the grid is passed to define resolution, data frame defines domain and range,
        # z for values
        Write_Tiff.write_file(z, ss, gridx, gridy, lat_min, lat_max, lon_min, lon_max)

        # clipping the tif here, using the cookie cutter and outputted tiff under write tiff function.
        Clip.clip()

        # printing that the process has completed
        print(f"Point shapefile outputted, {krig_type} kriging with {nlags} lags completed.")

        # prompting user to leave the program/or re-run
        while True:
            leave = input("Would you like to preform another kriging[y/n]?")
            if leave.lower() == "no" or leave.lower() == "n":
                quit()
            elif leave.lower() == 'yes' or leave.lower() == 'y':
                break
            else:
                print("Enter y/n or yes/no.")
                # TODO need to implement this in the GUI so we can perform multiple krigings without closing program
