import shutil
import os
import Kriging
import Write_Shape
import Write_Tiff
import Repo
import Chauv
import Clip
import proj
import LargeInterp
import UTMconvert


# main function
def dropSEQ(CSV, utmval, utmletterval, utmnumberval, SHP, seaval, lags_true, EXV, dropdown, dirtval):
    # create a dropping sequence that allows the gui to send the values to the back end
    home_dir = os.path.expanduser('~')
    # "naming" directories to store i/o operations
    directory1 = 'Input_CSV'
    directory2 = 'Input_SHP'
    directory3 = 'output_files'
    # parent directory
    parent_directory = 'Field-Interp-Tool'
    path0 = os.path.join(home_dir, 'Documents')
    path1 = os.path.join(path0, parent_directory)
    path2 = os.path.join(path1, directory1)  # CSV
    path3 = os.path.join(path1, directory2)  # SHP
    path4 = os.path.join(path1, directory3)  # output files
    # if the directories are not created, they will auto generate within the users documents folder
    if not os.path.exists(path1):
        os.mkdir(path1)
    else:
        path1 = path1
    if not os.path.exists(path2):
        os.mkdir(path2)
    else:
        path2 = path2
        dir1 = os.listdir(path2)
        if len(dir1) != 0:
            shutil.rmtree(path2)
            os.mkdir(path2)
            # deletes the contents of the input files if there are any present
    if not os.path.exists(path3):
        os.mkdir(path3)
    else:
        path3 = path3
        dir2 = os.listdir(path3)
        if len(dir2) != 0:
            shutil.rmtree(path3)
            os.mkdir(path3)
            # deletes the contents of the input files if there are any present
    if not os.path.exists(path4):
        os.mkdir(path4)
    else:
        path4 = path4
    # end of directory creation
    shutil.copy(CSV, path2)
    shutil.copy(SHP, path3)
    # copying over the input files to their input folders
    shpfull = (shutil.copy(SHP, path3))
    # used for the clipping function to determine the path of the copied shapefile
    shpname = os.path.splitext(SHP)
    # splitting the shapefiles original path to get just the name (represented in the variable "shpbase")
    shpbase = shpname[0]
    shpcpg = shpbase + '.cpg'
    shpdbf = shpbase + '.dbf'
    shpprj = shpbase + '.prj'
    shpsbn = shpbase + '.sbn'
    shpsbx = shpbase + '.sbx'
    shpxml = shpbase + '.shp.xml'
    shpshx = shpbase + '.shx'
    # getting the names of the other files linked to the shapefile
    shutil.copy(shpcpg, path3)
    shutil.copy(shpdbf, path3)
    shutil.copy(shpprj, path3)
    shutil.copy(shpsbn, path3)
    shutil.copy(shpsbx, path3)
    shutil.copy(shpxml, path3)
    shutil.copy(shpshx, path3)
    # copying all the other shapefiles over to the input directory
    long, lat, depth, fulldf, lengthfile = proj.tolatlon(path2)
    # proj splits the csv into 3 parts, lat, long, and depth
    # also returns the complete csv with negative values as well as the length of the file (will be used)
    fulldf = Chauv.chauv(depth, dirtval, long, lat, seaval)
    if utmval is True:
        lat, long, depth, dataframeutm = UTMconvert.utmconverter(utmletterval, utmnumberval, fulldf)
        # calls the function to convert from UTM coordinates to WGS84 EPSG 4326
        # returns a dataframe
        fulldf = dataframeutm
    else:
        fulldf = fulldf
    if lengthfile > 20000:
        LargeInterp.large(lat, long, depth, lags_true, EXV, dropdown, shpfull)
        # function for .csv files with more than 20000 points (this reduces computational time)
    shape, lat_max, lat_min, lon_max, lon_min = Repo.repo(long, lat, depth)
    # writing shape file
    Write_Shape.write_file(long, lat, depth)
    # searching for best parameters to try
    # ML is a boolean value from the GUI
    # prompting user to run kriging type
    # nlags checking
    while True:
        intlag = 0
        if lags_true == "6":
            intlag = 6
        elif lags_true == "8":
            intlag = 8
        elif lags_true == "10":
            intlag = 10
        elif lags_true == "15":
            intlag = 15
        elif lags_true == "20":
            intlag = 20
        else:
            intlag = 20
            # if the value is somehow undetermined, intlag (number of lags) will automatically be set at 20
        nlags = intlag
        try:
            nlags = intlag
            break
            # since the GUI returns a string, setting a new variable to a value will avoid a string to int cast
        except:
            continue
            # grabs the value from the gui received for exact values
    exact = EXV
    # START OF KRIGING #
    # we pass shape to mask the interpolation
    # Also going to error check in case of singular matrix or overload
    krig_type = dropdown
    z, ss, gridx, gridy = Kriging.kriging(fulldf, shape, lat_min, lat_max, lon_min, lon_max, nlags, krig_type, exact)
    # writing the tiff function, the grid is passed to define resolution, data frame defines domain and range,
    # z for values
    Write_Tiff.write_file(z, ss, gridx, gridy, lat_min, lat_max, lon_min, lon_max)
    # clipping the tif here, using the cookie cutter and outputted tiff underwrite tiff function.
    Clip.clip(shpfull)
