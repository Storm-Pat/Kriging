import numpy as np
import rasterio
#masking function alhumduallah
def write_file(z,ss,gridx,gridy,lat_min,lat_max,lon_min,lon_max):
    #making georeference
    #first defining domain and range of the projection, len x y have to be flipped respectivly for the correct resolution to hold.
    x=np.linspace(lon_min,lon_max,len(gridy))
    y=np.linspace(lat_min,lat_max,len(gridx))
    #making the transform using affine in rasterio
    #first setting the resolution
    res_x=(x[-1]-x[0])/len(x)
    res_y=(y[-1]-y[0])/len(y)
    #Then doing the transform on this, also will print transformation matrix for refference
    transform = rasterio.Affine.translation(x[0]-res_x/2,y[0]-res_y/2)*rasterio.Affine.scale(res_x,res_y)
    print("Affine Transformation of the Coordinates \n", transform)
    #first making a output tiff that is not cut
    with rasterio.open(
            'Outputs/z.tif',
            'w',
            driver='GTiff',
            height=z.shape[0],
            width=z.shape[1],
            count=1,
            dtype=z.dtype,
            transform=transform,
            crs='+proj=latlong',
    ) as dst:
        dst.write(z, 1)
    #writing error tiff that is not cut
    with rasterio.open(
            'Outputs/ss.tif',
            'w',
            driver='GTiff',
            height=ss.shape[0],
            width=ss.shape[1],
            count=1,
            dtype=ss.dtype,
            transform=transform,
            crs='+proj=latlong',
    ) as dst:
        dst.write(ss, 1)



