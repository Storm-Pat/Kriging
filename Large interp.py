import numpy as np
import naturalneighbor
import time

# natural neighbor for fast interpolation over large datasets?
start = time.time()

num_points = 10
# num_points refers to the amount of points to be interpolated, the lower the number, the faster the interpolation
# will be.
num_dimensions = 3
# 3D matrix, requires num_dimensions = 3
points = np.random.rand(num_points, num_dimensions)
# generates values within the specified matrix dimensions
values = np.random.rand(num_points)
# generates random points to be interpolated (will hopefully be replaced by real points in future)

grid_ranges = [[0, 100, 1], [0, 50, 1], [0, 20, 1]]
# defines how many values are going to be interpolated within the matrix given its size
nn_interpolated_values = naturalneighbor.griddata(points, values, grid_ranges)
# interpolates the matrix using natural neighbor
print(" ", nn_interpolated_values)
# prints out the interpolated values
print("%s seconds" % (time.time() - start))
# prints out the amount of time it took to interpolate the function
