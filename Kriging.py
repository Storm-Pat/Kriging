import numpy as np
import matplotlib.pyplot as plt
from pykrige.ok import OrdinaryKriging
def kriging(df,shape):
    #formatting the data
    x_val = df.iloc[:,0]
    y_val = df.iloc[:,1]
    depth = df.iloc[:,2]
    #doing the krieging
    OK =OrdinaryKriging(x_val,y_val,depth,variogram_model='power',verbose=True,enable_plotting=True,
                        coordinates_type="euclidean",nlags=8,weight=True,exact_values=True)
    #setting up the grid and executing the results over it
    ### MAKE USER INPUT VARIABLES
    gridx = np.arange(42.668798,42.670508,.000005,dtype = "float64")
    ###MAKE USER INPUT VARIABLES
    # right foot creep ouhh walking with that heater
    gridy = np.arange(-84.646129,-84.644108,.000005,dtype = "float64")
    #Look around and stay low make sure they dont see ya.
    #executing interp over defined grid, with the cookie cutter shape maksking outside values
    z, ss = OK.execute('grid',gridx,gridy,mask=shape)
    #have to apply this transpose for it all to work correctly, as the orgin is flipped in calculation
    z=z.T
    #making a plot of the krieging
    plt.imshow(z,origin='lower')
    plt.show()
    return z,ss,gridx,gridy