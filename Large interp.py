import numpy as np
import naturalneighbor
import time

# natural neighbor for fast interpolation over large datasets?
start = time.time()

num_points = 27000
num_dimensions = 3
# 3D matrix, requires num_dimensions = 3
points = np.random.rand(num_points, num_dimensions)
values = np.random.rand(num_points)

grid_ranges = [[0, 30, 1], [0, 30, 1], [0, 30, 1]]
nn_interpolated_values = naturalneighbor.griddata(points, values, grid_ranges)
print(" ", nn_interpolated_values)

print("%s seconds" % (time.time() - start))
