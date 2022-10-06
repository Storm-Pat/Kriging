import pandas as pd
import os
import glob
#Function to handel bathyboat data
def conc():
    oldpwd = os.getcwd()
    os.chdir('input')
    #creating a list of all the files in the csv directory
    all_files = [i for i in glob.glob('*.{}'.format('csv'))]
    #combining them
    df = pd.concat([pd.read_csv(f,names=['Latitude','Longitude','Depth_m','x','y','z','Time']) for f in all_files])
    #setting program directory back to home
    os.chdir(oldpwd)
    #settings the depth values negitive
    df.iloc[:,2] = -1*df.iloc[:,2]
    #filtering out objectivly wrong values (postive depth and nans)
    #first the nans
    df = df.dropna()
    df = df.reset_index(drop=True)
    #Then positive values
    for i in df.iloc[:,2]:
        if i > 0:
            df = df[df.Depth_m != i]
            df= df.reset_index(drop=True)
    return df

