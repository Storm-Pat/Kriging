import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import Chauv
import Repo
import os


def csvfile(CSV):
    return CSV


def bigboi(df, long_min, long_max, latit_min, latit_max):
    dirt = True
    dirtval = dirt
    df, dirt = Chauv.chauv(df, dirtval)
    home_dir = os.path.expanduser('~')
    path1 = 'Documents'
    path2 = os.path.join(home_dir, path1)
    path3 = 'Field-Interp-Tool'
    path4 = os.path.join(path2, path3)
    path5 = 'Input_CSV'
    path6 = os.path.join(path4, path5)
    os.path.exists(path6)
    CSV = os.listdir(path6)
    if os.path.exists(path6):
        df = pd.read_csv(*CSV)
        x = df.iloc[:, 0]
        y = df.iloc[:, 1]
        z = df.iloc[:, 2]
        print("1")
        # setting x gridd
        gridx = np.arange(x.min(), x.max(), .001, dtype="float64")
        # setting y grid
        gridy = np.arange(y.min(), y.max(), .001, dtype="float64")
        print("2")
        g = interpolate.interp2d(x, y, z, kind='quintic')
        preds = g(gridx, gridy)
        plt.imshow(preds)
        plt.show()
