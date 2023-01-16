import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from code import Chauv

df = pd.read_csv("input/SNDG00002_flyers_removed.csv")
lon_min=-84.646129
lon_max=-84.644108
lat_min=42.668798
lat_max=42.670508

def bigboi(df,lon_min,lon_max,lat_min,lat_max):
    df= Chauv.chauv(df)
    x=df.iloc[:,0]
    y=df.iloc[:,1]
    z=df.iloc[:,2]
    print("1")
    #setting x gridd
    gridx = np.arange(x.min(), x.max(), .001, dtype="float64")
    #setting y grid
    gridy=np.arange(y.min(),y.max(),.001, dtype="float64")
    print("2")
    g=interpolate.interp2d(x,y,z,kind='quintic')
    preds=g(gridx,gridy)
    plt.imshow(preds)
    plt.show()
bigboi(df,lon_min,lon_max,lat_min,lat_max)