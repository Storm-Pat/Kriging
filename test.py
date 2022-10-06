import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull, Delaunay, delaunay_plot_2d, Voronoi, voronoi_plot_2d
from scipy.spatial.distance import euclidean

from metpy.interpolate import geometry
from metpy.interpolate.points import natural_neighbor_point
np.random.seed(100)

pts = np.random.randint(0, 100, (10, 2))
xp = pts[:, 0]
yp = pts[:, 1]
zp = (pts[:, 0] * pts[:, 0]) / 1000

tri = Delaunay(pts)

fig, ax = plt.subplots(1, 1, figsize=(15, 10))
ax.ishold = lambda: True  # Work-around for Matplotlib 3.0.0 incompatibility
delaunay_plot_2d(tri, ax=ax)

for i, zval in enumerate(zp):
    ax.annotate(f'{zval} F', xy=(pts[i, 0] + 2, pts[i, 1]))

sim_gridx = [30., 60.]
sim_gridy = [30., 60.]

ax.plot(sim_gridx, sim_gridy, '+', markersize=10)
ax.set_aspect('equal', 'datalim')
ax.set_title('Triangulation of observations and test grid cell '
             'natural neighbor interpolation values')

members, circumcenters = geometry.find_natural_neighbors(tri, list(zip(sim_gridx, sim_gridy)))

val = natural_neighbor_point(xp, yp, zp, (sim_gridx[0], sim_gridy[0]), tri, members[0],
                             circumcenters)
ax.annotate(f'grid 0: {val:.3f}', xy=(sim_gridx[0] + 2, sim_gridy[0]))

val = natural_neighbor_point(xp, yp, zp, (sim_gridx[1], sim_gridy[1]), tri, members[1],
                             circumcenters)
ax.annotate(f'grid 1: {val:.3f}', xy=(sim_gridx[1] + 2, sim_gridy[1]))
plt.show()