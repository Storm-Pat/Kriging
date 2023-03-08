import numpy as np
import rasterio
import os

home_dir = os.path.expanduser('~')
parent_directory = 'Field-Interp-Tool'
directory1 = 'output_files'
path0 = os.path.join(home_dir, 'Documents')
path1 = os.path.join(path0, parent_directory)
path2 = os.path.join(path1, directory1)
path3 = os.path.join(path2, 'unclipped_kriging.tif')
path4 = os.path.join(path2, 'kriging_error_no_mask.tif')

# masking function alhumduallah
def write_file(z, ss, gridx, gridy, lat_min, lat_max, lon_min, lon_max):
    # making geo-reference first defining domain and range of the projection, len x y have to be flipped respectively
    # for the correct resolution to hold.
    x = np.linspace(lon_min, lon_max, len(gridy))
    y = np.linspace(lat_min, lat_max, len(gridx))
    # making the transform using affine in rasterio
    # first setting the resolution
    reso_x = (x[-1] - x[1]) / len(x)
    reso_y = (y[-1] - y[1]) / len(y)
    # Then doing the transform on this, also will print transformation matrix for reference
    transform = rasterio.Affine.translation(x[0] - reso_x / 2, y[0] - reso_y / 2) * rasterio.Affine.scale(reso_x, reso_y)
    # first making a output tiff that is not cut
    with rasterio.open(
            path3,
            'w',
            driver='GTiff',
            height=z.shape[0],
            width=z.shape[1],
            count=1,
            dtype=z.dtype,
            transform=transform,
            crs='WGS84',
    ) as dst:
        dst.write(z, 1)
    # writing error tiff that is not cut
    with rasterio.open(
            path4,
            'w',
            driver='GTiff',
            height=ss.shape[0],
            width=ss.shape[1],
            count=1,
            dtype=ss.dtype,
            transform=transform,
            crs='WGS84',
    ) as dst:
        dst.write(ss, 1)
