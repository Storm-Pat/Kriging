import pandas as pd
import numpy as np
import Repo
import Write_Shape
import Write_Tiff
import Kriging
import Clip


def large(lat, long, depth, lags_true, EXV, dropdown, shpfull):
    # larger datasets take a very long time, we are taking all the data and putting it over a sparse matrix
    # we then take the average of that grid and put it into a larger grid that has kriging applied to it
    # this will significantly reduce computational time
    zi, yi, xi = np.histogram2d(lat, long, bins=(140, 140),
                                weights=depth)
    counts, _, _ = np.histogram2d(lat, long, bins=(140, 140))
    zi = zi / counts
    # correcting for the difference in zi and the axis
    xi = np.linspace(xi.min(), xi.max(), len(zi), zi.shape[0], dtype="float64")
    yi = np.linspace(yi.min(), yi.max(), len(zi), zi.shape[1], dtype="float64")
    zi = np.ma.masked_invalid(zi)
    xx, yy = np.meshgrid(xi, yi)
    # get valid vals
    x1 = xx[~zi.mask]
    y1 = yy[~zi.mask]
    z1 = zi[~zi.mask]
    df1 = pd.DataFrame({'Longitude': y1, 'Latitude': x1, 'Depth_m': z1}).astype("float64")
    shape, lat_max, lat_min, lon_max, lon_min = Repo.repo(long, lat, depth)
    # writing shape file
    idx = pd.IndexSlice
    long = df1.iloc[idx[:, 0]]
    lat = df1.iloc[idx[:, 1]]
    depth = df1.iloc[idx[:, 2]]
    fulldataframe = [long, lat, depth]
    Write_Shape.write_file(long, lat, depth)
    print("onto kriging")
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
    z, ss, gridx, gridy = Kriging.kriging(fulldataframe, shape, lat_min, lat_max, lon_min, lon_max, nlags, krig_type, exact)
    # writing the tiff function, the grid is passed to define resolution, data frame defines domain and range,
    # z for values
    Write_Tiff.write_file(z, ss, gridx, gridy, lat_min, lat_max, lon_min, lon_max)
    # clipping the tif here, using the cookie cutter and outputted tiff underwrite tiff function.
    Clip.clip(shpfull)
