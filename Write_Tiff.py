import numpy as np
import rasterio
#masking function alhumduallah
def write_file(z,gridx,gridy):
    #making georeference
    #first defining domain and range of the projection, len x y have to be flipped respectivly for the correct resolution to hold.
    ### MAKE USER INPUT VARIABLES
    x=np.linspace(-84.646129,-84.644108,len(gridy))
    y=np.linspace(42.668798,42.670508,len(gridx))
    #making the transform using affine in rasterio
    #first setting the resolution
    res_x=(x[-1]-x[0])/len(x)
    res_y=(y[-1]-y[0])/len(y)
    #Then doing the transform on this, also will print transformation matrix for refference
    transform = rasterio.Affine.translation(x[0]-res_x/2,y[0]-res_y/2)*rasterio.Affine.scale(res_x,res_y)
    print("Affine Transformation of the Coordinates", transform)
    #first making a output tiff that is not cut
    with rasterio.open(
            'z.tff',
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



