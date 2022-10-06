import pyproj as proj
import os
import glob
import pandas as pd
#Function to handel Iver 3 data
def tolatlon():
    #reading in Iver 3 csv data
    oldpwd = os.getcwd()
    os.chdir('input')
    #creating a list of all the files in the csv directory
    all_files = [i for i in glob.glob('*.{}'.format('csv'))]
    df = pd.concat([pd.read_csv(f) for f in all_files])
    #setting program directory back to home
    os.chdir(oldpwd)
    #settings the depth values negitive
    df.iloc[:,2] = -1*df.iloc[:,2]
    #filtering out objectivly wrong values (postive depth and nans)
    #first the nans
    df = df.dropna()
    df = df.reset_index(drop=True)
    #creating proj option
    myProj = proj.Proj(proj='utm',zone=16,ellps='WGS84')
    lon,lat=myProj(df['X'].values,df['Y'].values,inverse=True)
    df.iloc[:,0]=lon
    df.iloc[:,1]=lat
    df = df.rename(columns={'X':'Longitude','Y':'Latitude','Z': 'Depth_m'})
    print(df.memory_usage())
    return df