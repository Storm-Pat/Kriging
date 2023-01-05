import numpy as np
import matplotlib.pyplot as plt
from pykrige.ok import OrdinaryKriging
import multiprocessing


def kriging(df, shape, lat_min, lat_max, lon_min, lon_max, nlags, krig_type, exact=False):
    # formatting the data
    x_val = df.iloc[:, 0]
    y_val = df.iloc[:, 1]
    depth = df.iloc[:, 2]
    # doing the kriging
    OK = OrdinaryKriging(x_val, y_val, depth, variogram_model=krig_type, verbose=True, enable_plotting=True,
                         coordinates_type="euclidean", nlags=nlags, weight=True, exact_values=exact, pseudo_inv=True)
    # setting up the grid and executing the results over it

    # base resolution is 1 pixel per meter
    resofull = 0.00001
    # .00001 (roughly 3ft by 3ft, translates to 1 square meter **roughly**)
    # TODO ask the user to enter a value for the resolution (or have option in GUI) then do the math to convert
    print(lat_min)
    print(lat_max)
    gridx = np.arange(lat_min, lat_max, resofull, dtype="float64")
    gridy = np.arange(lon_min, lon_max, resofull, dtype="float64")
    # executing interp over defined grid, with the cookie cutter shape masking outside values
    z, ss = (OK.execute('grid', gridx, gridy, mask=shape))
    # TODO try and get multiprocessing working on this
    # have to apply this transpose for it all to work correctly, as the origin is flipped in calculation
    z = z.T
    ss = ss.T
    # making a plot of the kriging
    plt.figure(1)
    plt.imshow(z, origin='lower')
    plt.title("Kriging Results")

    plt.figure(2)
    plt.imshow(ss, origin="lower")
    plt.title("Kriging Error")
    plt.show()
    return z, ss, gridx, gridy
