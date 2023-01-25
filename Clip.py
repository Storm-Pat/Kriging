import rasterio
import fiona
import rasterio.mask
import time
import Main


def clip():
    csv_gui = None
    shp_gui = None
    mach_learn = None
    lags_true_gui = None
    exval = None
    krigtype = None
    dirt = None

    CSV, SHP, ML, lags_true, EXV, dropdown, dirtval = Main.guidrop(csv_gui, shp_gui, mach_learn, lags_true_gui, exval,
                                                              krigtype, dirt)
    # reprojecting shape file
    with fiona.open(SHP, 'r') as f:
        shapes = [feature["geometry"] for feature in f]
    # opening raster and clipping now inshallah (I copied this context manager from the rasterio wiki lol)
    # https://rasterio.readthedocs.io/en/latest/topics/masking-by-shapefile.html pretty fucking niftey
    with rasterio.open('output_files/unclipped_kriging.tif') as src:
        out_image, out_transform = rasterio.mask.mask(src, shapes, invert=False)
        out_meta = src.meta
        # raster output data, once again straight from the wiki
    out_meta.update({"driver": "GTiff",
                     "height": out_image.shape[1],
                     "width": out_image.shape[2],
                     "transform": out_transform})
    # outputting the sliced tiff
    with rasterio.open('output_files/kriging_with_mask.tif', 'w', **out_meta) as f:
        f.write(out_image)
    # Same as above but now clipping the erorr
    with rasterio.open('output_files/kriging_error_no_mask.tif') as src:
        out_image, out_transform = rasterio.mask.mask(src, shapes, invert=False)
        out_meta = src.meta
        # raster output data, once again straight from the wiki
    out_meta.update({"driver": "GTiff",
                     "height": out_image.shape[1],
                     "width": out_image.shape[2],
                     "transform": out_transform})
    # outputting the sliced tiff
    with rasterio.open('output_files/kriging_error_with_mask.tif', 'w', **out_meta) as f:
        f.write(out_image)
    # a error about projections will be thrown over the fact the shapefile was converted, so this is here for
    # readability
    time.sleep(2)
