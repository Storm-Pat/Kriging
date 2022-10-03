#!./usr/bin/env python
import os
import shutil
import Kriging
import Write_Shape
import Conc
import Write_Tiff
import Clip
import Repo
import Chauv
import Switch
import CV

#main function
if __name__ == '__main__':
    #truncating the cookie cutters, shapefiles, and outputtiff folder here
    #starting with the cookie cutters
    shutil.rmtree('cookie_cutters')
    os.mkdir('cookie_cutters')
    #same but with point shapefiles
    shutil.rmtree('Outputs')
    os.mkdir('Outputs')
    #really the main while loop where the magic happens after intializing everything
    while True:
        #concatinating and labeling the data
        df=Conc.conc()
        #cleaning algorithm,returns chosen dataframe
        df = Chauv.chauv(df)
        #reporojecting the shapefile
        shape,lat_max,lat_min,lon_max,lon_min = Repo.repo()
        #writing shape file
        Write_Shape.write_file(df)
        while True:
            ans = input("Would you like to set a custom domain and range[y/n]?")
            if ans.lower() == "yes" or ans.lower() == "y":
                while True:
                    lon_min = input('Please enter your minimum longitude')
                    lon_max = input('Please enter your maximum longitude')
                    lat_min = input('Please enter your minimum latitude')
                    lat_max = input('Please enter your maximum latitude')
                    # exception checking the inputs
                    try:
                        # casting the points to floats to allow computation
                        lon_min = float(lon_min)
                        lon_max = float(lon_max)
                        lat_min = float(lat_min)
                        lat_max = float(lat_max)
                    except:
                        print("Please enter a valid number")
                        continue

                    # checking to see if the inputed values are valid domain and ranges
                    if lat_min >= lat_max:
                        print("Invalid range, minimum lattidude is greater than or equal to maximum latitude")
                        continue
                    if lon_min >= lon_max:
                        print("Invalid domain, minimum longitude greater than or equal to maximum longitude")
                        continue
                    break
                break
            elif ans.lower() == "no" or ans.lower() == "n":
                break
            else:
                print("Enter a yes/no or y/n")
        ####### UGLY ASS YANDERE DEV USER INPUT BOILLERPLATE #############
        #If only python 3.9 suported using match as a switch statement
        #serching for best parameters to try
        while True:
            i = input("Would you like to use ML to get the best parameters[y/n] (Note: this takes a while)")
            if i.lower() == "yes" or i.lower() == "y":
                #calling our wonderfull ML function
                CV.cv(df)
                break
            elif i.lower() == "no" or i.lower() == "n":
                break
            else:
                print("Enter a valid input")
        #prompting user to run kriging type
        krig_type = Switch.switch()
        #nlags checking
        while True:
            nlags=input("Please enter an Integer for the number of variogram lags")
            try:
                nlags=int(nlags)
                break
            except:
                print("Please enter an integer or number")
                continue
        #allow to user to enable or disable wheights
        while True:
            weights=input("Would you like to apply weights[y/n]")
            if weights.lower() == "yes" or weights.lower() == "y":
                weights = True
                break
            elif weights.lower() == "no" or weights.lower() == "n":
                weights = False
                break
            else:
                print("Enter yes/no or y/n")
        #prompting user if they want to use a pseduo inverse matrix
        while True:
            PI = input("Would you like to use a pseudo inverse matrix[y/n]")
            if PI.lower() == "yes" or PI.lower() == "y":
                PI = True
                break
            elif PI.lower() == "no" or PI.lower() == "n":
                PI = False
                break
            else:
                print("Please enter yes/no or y/n")
        #prompting the user to select the wheter to use exact values or not
        while True:
            exact = input("Would you like to use exact values[y/n]")
            if exact.lower() == "yes" or exact.lower() == "y":
                exact = True
                break
            elif exact.lower() == "no" or exact.lower() == "n":
                exact = False
                break
            else:
                print("Please enter yes/no or y/n")

        #### START OF KRIGING ####
        #we pass shape to mask the interpolation
        #Also going to error check in case of singular matrix or overload
        z,ss,gridx,gridy = Kriging.kriging(df,shape,lat_min,lat_max,lon_min,lon_max,nlags,krig_type,weights,PI,exact)
        #writting the tiff function, the grid is passed to define resolution, data frame defines domain and range,z for values
        Write_Tiff.write_file(z,ss,gridx,gridy,lat_min,lat_max,lon_min,lon_max)

        #clipping the tif here, using the cookie cutter and outputted tiff under write tiff function.
        Clip.clip()

        #printing that the process has completed
        print(f"Point shapefile outputted, {krig_type} kriging with {nlags} lags completed.")

        #prompting user to leave the program/or re run
        while True:
            leave = input("Would you like to preform another kriging[y/n]?")
            if leave.lower()=="no" or leave.lower()=="n":
                quit()
            elif leave.lower()=='yes' or leave.lower()=='y':
                break
            else:
                print("Enter y/n or yes/no.")





