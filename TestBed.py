import multiprocessing

import Kriging
import Write_Shape
import Conc
import Write_Tiff
import Clip
import Repo
import Chauv
import tkinter as Tk
from tkinter import *
#multiprocessing function

#main function
if __name__ == '__main__':
    #Set up gui
    #gui = Tk(className='GENEX script-main input')
    #gui.geometry("340x460")
    #put csvs here
    #put og shapes
    #LONG
    #LAT
    #Nlags
    #booleans (weight and exact values)
    #gui.mainloop()

    #TODO, Have user enter path to the csv files, remeber to fix path in conc function
    #TODO, Add a user defined domain and range, cause shape file D-R varies wildley, maybe can auto in future.
    #setting file path, the user will do this later
    direct = '/home/pabritt/Krig'

    #TODO: FRONTEND: HAVE USER DEFINE OUTPUT FILE LOCATION AND NAME
    #outputfile stuff

    #reporojecting the shapefile
    #TODO: FRONTEND: have user input mask shapefile
    shape = Repo.repo()

    #concatinating and labeling the data
    df=Conc.conc(direct)

    #TODO: ADD CLEANNG ALGORITHM
    #cleaning algorithm
    #returns chosen dataframe
    Chauv.chauv(df)

    #writing shape file
    Write_Shape.write_file(df)

    #### START OF KRIGING ####
    #with multiprocessing.Pool() as pool:
        #for result in pool.map(Kriging.kriging,df,shape):
            #z,ss,gridx,gridy= result
    #we pass shape to mask the interpolation
    z,ss,gridx,gridy = Kriging.kriging(df,shape)

    #writting the tiff function, the grid is passed to define resolution, data frame defines domain and range,z for values
    Write_Tiff.write_file(z,gridx,gridy)

    #clipping the tif here, using the cookie cutter and outputted tiff under write tiff function.
    Clip.clip()

