import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
from osgeo import gdal
from scipy.interpolate import griddata
import fiona
import rasterio.mask
df = pd.read_csv("/home/pabritt/Krig/testing data/SchoharieBridge_Oct2022_Sonar_AllSensors_Clean_Combined.csv")
zi,yi,xi = np.histogram2d(df.iloc[:,1], df.iloc[:,0],bins=(100,100), weights=df.iloc[:,2], normed=False)
counts, _, _= np.histogram2d(df.iloc[:,1],df.iloc[:,0],bins=(100,100))
zi=zi/counts
shape=gpd.read_file("input/SchoharieCrk_RiverBoundaryMask_Clipped.shp")
shit = shape.to_crs(epsg=3857)
# reading it back out to a file under the cookie cutters, seperate from the og shapefiles
shit.to_file(driver='ESRI Shapefile', filename=f"cookie_cutters")
# Shit becomes shape again in main lol
# grabbing the min and maxes
extrema = shit.bounds
lon_min = float(extrema['minx'])
lon_max = float(extrema['maxx'])
lat_min = float(extrema['miny'])
lat_max = float(extrema['maxy'])
#making csv here from geotiff to run kriging
ds=gdal.Open('wew.tif')
#correcting for the diffrence in zi and the axis
xi=np.linspace(xi.min(),xi.max(),len(zi),zi.shape[0])
yi=np.linspace(yi.min(),yi.max(),len(zi),zi.shape[1])
zi=np.ma.masked_invalid(zi)
xx,yy=np.meshgrid(xi,yi)
#get valid vals
x1=xx[~zi.mask]
y1=yy[~zi.mask]
zi=zi[~zi.mask]
print(len(x1),len(y1),len(zi),len(xx),len(yy))
Z = griddata((x1,y1),zi,(xx,yy),method='cubic')
print(Z)
plt.figure()
plt.imshow(Z,origin='lower')
plt.show()
x=np.linspace(df.iloc[:,1].min(),df.iloc[:,1].max(),len(xi))
y=np.linspace(df.iloc[:,0].min(),df.iloc[:,0].max(),len(yi))
#making the transform using affine in rasterio
#first setting the resolution
res_x = (xi[-1] - xi[0]) / len(xi)
res_y = (yi[-1] - yi[0]) / len(yi)
#Then doing the transform on this, also will print transformation matrix for refference
transform = rasterio.Affine.translation(x[0]-res_x/2,y[0]-res_y/2)*rasterio.Affine.scale(res_x,res_y)
print("Affine Transformation of the Coordinates", transform)
with rasterio.open(
    'wew.tif',
    'w',
    driver='GTiff',
    height=Z.shape[0],
    width=Z.shape[1],
    count=1,
    dtype=Z.dtype,
    transform=transform,
) as dst:
    dst.write(Z, 1)
with fiona.open('/home/pabritt/Krig/cookie_cutters/cookie_cutters.shp','r') as f:
    shapes = [feature["geometry"] for feature in f]
#openning raster and clipping now inshallah (I copied this context manager from the rasterio wiki lol)
#https://rasterio.readthedocs.io/en/latest/topics/masking-by-shapefile.html pretty fucking niftey
with rasterio.open('wew.tif') as src:
    out_image,out_transform= rasterio.mask.mask(src,shapes,invert=False)
    out_meta = src.meta
    #raster output data, once again straight from the wiki
out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform,})
#outputting the sliced tiff
with rasterio.open('wew_mask.tif', 'w', **out_meta) as f:
    f.write(out_image)
