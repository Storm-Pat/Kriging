import os
import glob
import pandas as pd
#Function to handel Iver 3 data
def tolatlon():
    #reading in Iver 3 csv data
    oldpwd = os.getcwd()
    os.chdir('Kriging/input')
    #creating a list of all the files in the csv directory
    all_files = [i for i in glob.glob('*.{}'.format('csv'))]
    df = pd.concat([pd.read_csv(f) for f in all_files])
    #setting program directory back to home
    os.chdir(oldpwd)
    #settings the depth values negitive
    df.iloc[:,2] = -1*df.iloc[:,2]
    #removing positive values
    df = df[df.iloc[:,2] >= 0]
    return df
