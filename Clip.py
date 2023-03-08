import rasterio
import fiona
import rasterio.mask
import os
import geopandas

home_dir = os.path.expanduser('~')
parent_directory = 'Field-Interp-Tool'
directory1 = 'output_files'
directory2 = 'Input_SHP'
path0 = os.path.join(home_dir, 'Documents')
path1 = os.path.join(path0, parent_directory)
path2 = os.path.join(path1, directory1)
shaper = os.path.join(path1, directory2)
path3 = os.path.join(path2, 'unclipped_kriging.tif')
path4 = os.path.join(path2, 'kriging_error_no_mask.tif')
path5 = os.path.join(path2, 'kriging_with_mask.tif')
path6 = os.path.join(path2, 'kriging_error_with_mask.tif')


def clip(SHP):
    shapepath = os.path.join(shaper, SHP)
    # reprojecting shape file

    with fiona.open(shapepath, 'r') as f:
        shapes = [feature["geometry"] for feature in f]
    # opening raster and clipping now inshallah (I copied this context manager from the rasterio wiki lol)
    # https://rasterio.readthedocs.io/en/latest/topics/masking-by-shapefile.html pretty fucking niftey
    with rasterio.open(path3) as src:
        out_image, out_transform = rasterio.mask.mask(src, shapes, invert=False)
        out_meta = src.meta
        # raster output data, once again straight from the wiki
    out_meta.update({"driver": "GTiff",
                     "height": out_image.shape[1],
                     "width": out_image.shape[2],
                     "transform": out_transform})
    # outputting the sliced tiff
    with rasterio.open(path5, 'w', **out_meta) as f:
        f.write(out_image)
    # Same as above but now clipping the erorr
    with rasterio.open(path4) as src:
        out_image, out_transform = rasterio.mask.mask(src, shapes, invert=False)
        out_meta = src.meta
        # raster output data, once again straight from the wiki
    out_meta.update({"driver": "GTiff",
                     "height": out_image.shape[1],
                     "width": out_image.shape[2],
                     "transform": out_transform})
    # outputting the sliced tiff
    with rasterio.open(path6, 'w', **out_meta) as f:
        f.write(out_image)
    # a error about projections will be thrown over the fact the shapefile was converted, so this is here for
    # readability
