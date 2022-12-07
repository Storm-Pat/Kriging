import numpy as np
import matplotlib.pyplot as plt
from pykrige.ok import OrdinaryKriging
def kriging(df,shape,lat_min,lat_max,lon_min,lon_max,nlags,krig_type,weights,PI,exact):
    #formatting the data
    x_val = df.iloc[:,0]
    y_val = df.iloc[:,1]
    depth = df.iloc[:,2]
    print(df)
    #doing the krieging
    OK=OrdinaryKriging(x_val,y_val,depth,variogram_model=krig_type,verbose=True,enable_plotting=True,
                        coordinates_type="euclidean",nlags=nlags,weight=weights,exact_values=exact, pseudo_inv=PI)
    #setting up the grid and executing the results over it
    gridx = np.arange(lat_min,lat_max,.000009,dtype="float64")
    # right foot creep ouhh walking with that heater
    gridy = np.arange(lon_min,lon_max,.000009,dtype="float64")
    #Look around and stay low make sure they dont see ya.
    #executing interp over defined grid, with the cookie cutter shape maksking outside values
    z, ss = OK.execute('grid',gridx,gridy,mask=shape)
    #have to apply this transpose for it all to work correctly, as the orgin is flipped in calculation
    z=z.T
    ss=ss.T
    #making a plot of the krieging
    plt.figure(1)
    plt.imshow(z,origin='lower')
    plt.title("Kriging Results")

    plt.figure(2)
    plt.imshow(ss,origin="lower")
    plt.title("Kriging Error")
    plt.show()
    return z,ss,gridx,gridy
