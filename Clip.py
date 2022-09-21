import rasterio
import fiona
import rasterio.mask
def clip():
    #reprojecting shape file
    with fiona.open('/home/pabritt/Krig/cookie_cutters/I96Billwood_GrandRiverMask.shp','r') as f:
        shapes = [feature["geometry"] for feature in f]
    #openning raster and clipping now inshallah (I copied this context manager from the rasterio wiki lol)
    #https://rasterio.readthedocs.io/en/latest/topics/masking-by-shapefile.html pretty fucking niftey
    with rasterio.open('z.tff') as src:
        out_image,out_transform= rasterio.mask.mask(src,shapes,invert=False)
        out_meta = src.meta
        #raster output data, once again straight from the wiki
    out_meta.update({"driver": "GTiff",
                     "height": out_image.shape[1],
                     "width": out_image.shape[2],
                     "transform": out_transform})
    #outputting the sliced tiff
    with rasterio.open('z_mask.tff','w',**out_meta) as f:
        f.write(out_image)
