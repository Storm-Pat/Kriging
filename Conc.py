import pandas as pd
import os
import glob
def conc(direct):
    os.chdir(direct + '/csvs (copy)')
    #creating a list of all the files in the csv directory
    all_files = [i for i in glob.glob('*.{}'.format('csv'))]
    #combining them
    df = pd.concat([pd.read_csv(f,names=['Latitude','Longitude','Depth_m','x','y','z','Time']) for f in all_files])
    #setting program directory back to home
    os.chdir(direct)
    return df

