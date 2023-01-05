import rasterio
import fiona
import rasterio.mask
import time
def clip():
    #reprojecting shape file
    with fiona.open('/home/pabritt/Krig/cookie_cutters/cookie_cutters.shp','r') as f:
        shapes = [feature["geometry"] for feature in f]
    #opening raster and clipping now inshallah (I copied this context manager from the rasterio wiki lol)
    #https://rasterio.readthedocs.io/en/latest/topics/masking-by-shapefile.html pretty fucking niftey
    with rasterio.open('Kriging/Outputs/z.tif') as src:
        out_image,out_transform= rasterio.mask.mask(src,shapes,invert=False)
        out_meta = src.meta
        #raster output data, once again straight from the wiki
    out_meta.update({"driver": "GTiff",
                     "height": out_image.shape[1],
                     "width": out_image.shape[2],
                     "transform": out_transform})
    #outputting the sliced tiff
    with rasterio.open('Kriging/Outputs/z_mask.tif', 'w', **out_meta) as f:
        f.write(out_image)
    #Same as above but now clipping the erorr
    with rasterio.open('Kriging/Outputs/ss.tif') as src:
        out_image, out_transform = rasterio.mask.mask(src, shapes, invert=False)
        out_meta = src.meta
        # raster output data, once again straight from the wiki
    out_meta.update({"driver": "GTiff",
                     "height": out_image.shape[1],
                     "width": out_image.shape[2],
                     "transform": out_transform})
    # outputting the sliced tiff
    with rasterio.open('Kriging/Outputs/ss_mask.tif', 'w', **out_meta) as f:
        f.write(out_image)
    #a error about projections will be thrown over the fact the shapefile was converted, so this is here for readability
    time.sleep(2)