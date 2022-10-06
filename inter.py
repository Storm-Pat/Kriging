from scipy import spatial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull, Delaunay, delaunay_plot_2d, Voronoi, voronoi_plot_2d
from scipy.spatial.distance import euclidean
import proj
from metpy.interpolate import geometry
from metpy.interpolate.points import natural_neighbor_point
###TESTING SHTUFF
import pandas as pd
lon_min=-84.64624
lon_max=-84.64414
lat_min=42.6687
lat_max=42.67067
def interp(lon_min,lon_max,lat_min,lat_max):
    #test repo
    df=proj.tolatlon()
    tri=spatial.Delaunay(df.iloc[:,0:2])
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    ax.ishold = lambda: True  # Work-around for Matplotlib 3.0.0 incompatibility
    delaunay_plot_2d(tri, ax=ax)

    for i, zval in enumerate(df.iloc[:,2]):
        ax.annotate(f'{zval} F', xy=(df.iloc[i, 0] + 2, df.iloc[i, 1]))

    sim_gridx = np.linspace(lat_min,lat_max,1000,dtype="float64")
    # right foot creep ouhh walking with that heater
    sim_gridy = np.linspace(lon_min,lon_max,1000,dtype="float64")

    ax.plot(sim_gridx, sim_gridy, '+', markersize=10)
    ax.set_aspect('equal', 'datalim')
    ax.set_title('Triangulation of observations and test grid cell '
                 'natural neighbor interpolation values')

    plt.show()
interp(lon_min,lon_max,lat_min,lat_max)

