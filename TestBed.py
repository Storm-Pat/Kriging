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

#main function
if __name__ == '__main__':
    #truncating the cookie cutters, and shapefiles folder here
    #starting with the cookie cutters
    shutil.rmtree('cookie_cutters')
    os.mkdir('cookie_cutters')
    #same but with point shapefiles
    shutil.rmtree('Shape Files')
    os.mkdir('Shape Files')
    # setting file path, the user will do this later
    direct = '/home/pabritt/Krig'
    #intial values

    while True:
        lon_min=input('Please enter your minimum longitude')
        lon_max=input('Please enter your maximum longitude')
        lat_min=input('Please enter your minimum latitude')
        lat_max=input('Please enter your maximum latitude')
        #exception checking the inputs
        try:
            # casting the points to floats to allow computation
            lon_min=float(lon_min)
            lon_max=float(lon_max)
            lat_min=float(lat_min)
            lat_max=float(lat_max)
        except:
            print("Please enter a valid number")
            continue

        #checking to see if the inputed values are valid domain and ranges
        if lat_min >= lat_max:
            print("Invalid range, minimum lattidude is greater than or equal to maximum latitude")
            continue
        if lon_min >= lon_max:
            print("Invalid domain, minimum longitude greater than or equal to maximum longitude")
            continue
        break

    #really the main while loop where the magic happens after intializing everything
    while True:
        #concatinating and labeling the data
        df=Conc.conc(direct)
        #cleaning algorithm,returns chosen dataframe
        df = Chauv.chauv(df)
        #asking for kriging type
        krig_type = Switch.switch()
        print(krig_type)
        #nlags checking
        while True:
            nlags=input("Please enter an Integer for the number of variogram lags")
            try:
                nlags=int(nlags)
                break
            except:
                print("Please enter an integer or number")
                continue

        #reporojecting the shapefile
        shape = Repo.repo()

        #writing shape file
        Write_Shape.write_file(df)

        #### START OF KRIGING ####
        #we pass shape to mask the interpolation
        z,ss,gridx,gridy = Kriging.kriging(df,shape,lat_min,lat_max,lon_min,lon_max,nlags,krig_type)

        #writting the tiff function, the grid is passed to define resolution, data frame defines domain and range,z for values
        Write_Tiff.write_file(z,gridx,gridy,lat_min,lat_max,lon_min,lon_max)

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

        #flow controll for reseting or keeping domain and range
        while True:
            t_f= input("Would you like to keep the same domain and range[y/n]")
            if t_f.lower() == "yes" or t_f.lower() == "y":
                print("Keeping the same domain and range")
                break
            elif t_f.lower()=="no" or t_f.lower()=="n":
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
            else:
                print("Please enter yes/no or y/n")
                continue





