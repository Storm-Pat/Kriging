import Kriging
import Write_Shape
import Conc
import Write_Tiff
import Clip
import Repo
from multiprocessing import Pool
from multiprocessing import Lock
import os
#main function
if __name__ == '__main__':
    #setting file path, the user will do this later
    #TODO, Add a user defined domain and range, cause shape file D-R varies wildley, maybe can auto in future.
    #TODO, Have user enter path to the csv files, remeber to fix path in conc function
    #TODO add multi-threading to io tasks, add multi processing to krigging
    direct = '/home/pabritt/Krig'
    #reporojecting the shapefile
    #TODO: have user enter path of mask
    shape = Repo.repo()
    #concatinating and labeling the data
    df=Conc.conc(direct)
    #writing shape file
    Write_Shape.write_file(df)
    #### START OF KRIGING ####
    #we pass shape to mask the interpolation
    z,ss,gridx,gridy = Kriging.kriging(df,shape)
    #writting the tiff function, the grid is passed to define resolution, data frame defines domain and range,z for values
    Write_Tiff.write_file(z,gridx,gridy)
    #clipping the tif here, using the cookie cutter and outputted tiff under write tiff function.
    Clip.clip()

