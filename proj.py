import os
import glob
import pandas as pd


# Function to handle Iver 3 data
def tolatlon():
    # since iver3 datasets tend to be very large, we are taking all the data and putting it over a sparse matrix
    # we then take the average of that grid and put it into a larger grid that has kriging applied to it
    # this will significantly reduce computational time
    home_dir = os.path.expanduser('~')
    parent_directory = 'Field-Interp-Tool'
    directory1 = 'Input_CSV'
    path0 = os.path.join(home_dir, 'Documents')
    path1 = os.path.join(path0, parent_directory)
    path2 = os.path.join(path1, directory1)
    # "re-pointing" to the directory for the input csv file
    # reading in Iver 3 csv data
    oldpwd = os.getcwd()
    os.chdir(path2)
    # checking the path
    # creating a list of all the files in the csv directory
    all_files = [i for i in glob.glob('*.{}'.format('csv'))]
    df = pd.concat([pd.read_csv(f) for f in all_files])
    # setting program directory back to home
    os.chdir(oldpwd)
    # settings the depth values negative
    df.iloc[:, 2] = -1 * df.iloc[:, 2]
    # removing positive values
    df = df[df.iloc[:, 2] >= 0]
    return df
