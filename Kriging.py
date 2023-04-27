import numpy as np
import matplotlib.pyplot as plt
from pykrige.ok import OrdinaryKriging
import os
import pandas as pd
import rasterio
import rasterio.mask
import fiona
import multiprocessing
import UTMconvert


# TODO figure out a way to include multiprocessing in this section
# the section for kriging is very slow and could benefit from kriging, although it may already utilize MP

home_dir = os.path.expanduser('~')
directory = 'output_files'
parent_directory = 'Field-Interp-Tool'
path0 = os.path.join(home_dir, 'Documents')
path1 = os.path.join(path0, parent_directory)
path2 = os.path.join(path1, 'Kriging-result.tif')
path3 = os.path.join(path1, 'Kriging-error.tif')

def kriging(fulldf, shape, lat_min, lat_max, lon_min, lon_max, nlags, krig_type, exact, letter, number):
    # formatting the data
    # doing the kriging
    idx = pd.IndexSlice
    print(type(fulldf))
    if type(fulldf) == list:
        lat = fulldf[0]
        long = fulldf[1]
        depth = fulldf[2]
    else:
        lat = fulldf.iloc[idx[:, 0]]
        long = fulldf.iloc[idx[:, 1]]
        depth = fulldf.iloc[idx[:, 2]]
    OK = OrdinaryKriging(lat, long, depth,
                         variogram_model=krig_type, verbose=True, enable_plotting=True, coordinates_type="euclidean",
                         nlags=nlags, exact_values=exact, pseudo_inv=True)
    # setting up the grid and executing the results over it

    # base resolution is 1 pixel per meter
    resofull = 0.000005
    # .00001 (roughly 3ft by 3ft, translates to 1 square meter **roughly**)

    # created grid in order to execute the interpolation over
    gridx = np.arange(start=lat_min, stop=lat_max, step=resofull)
    gridy = np.arange(start=lon_min, stop=lon_max, step=resofull)
    # executing interpolation over defined grid, with the cookie cutter shape masking outside values
    z, ss = (OK.execute("grid", gridx, gridy, mask=shape))
    print(gridx)
    print(gridy)
    # UTMconvert.returnutm(letter, number, gridx, gridy)
    # have to apply this transpose for it all to work correctly, as the origin is flipped in calculation
    z = z.T
    ss = ss.T
    # making a plot of the kriging
    plt.figure(1)
    plt.imshow(z, origin="lower")
    plt.title("Kriging Results")

    plt.figure(2)
    plt.imshow(ss, origin="lower")
    plt.title("Kriging Error")
    plt.show()
    return z, ss, gridx, gridy
