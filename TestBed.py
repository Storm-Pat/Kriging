from tkinter import *
import tkinter as tk
import os
import Clip
import Conc
import Kriging
import Repo
import Write_Shape
import Write_Tiff

# multiprocessing function

# main function
if __name__ == '__main__':
    # Set up gui
    gui = Tk(className='GENEX script-main input')
    gui.geometry("340x460")


    def main():
        csv_f = tk.StringVar()
        CSV = csv_f.get()
        csv_f.set("")
        inpone = tk.Label(text="Input .csv file(s) or folder.")
        entry_one = tk.Entry(
            gui,
            textvariable=csv_f,
            fg="red",
            bg="white",
            width=40
        )
        # put csvs here
        shp_f = tk.StringVar()
        SHP = shp_f.get()
        shp_f.set("")
        inp_two = tk.Label(text="Input .shp file(s) or folder.")
        entry_two = tk.Entry(
            gui,
            textvariable=shp_f,
            fg="red",
            bg="white",
            width=40
        )
        space0 = tk.Label(text="______________________________________________________________________________")
        space0.pack()
        inpone.pack()
        entry_one.pack()
        inp_two.pack()
        entry_two.pack()
        space1 = tk.Label(text="______________________________________________________________________________")
        space1.pack()
        # put og shapes
        long_min = tk.DoubleVar()
        LONG_MIN = long_min.get()
        long_min.set = float
        longmin = tk.Label(gui, text="Minimum longitude: ")
        longmin_txt = tk.Entry(
            gui,
            textvariable=long_min,
            fg="blue",
            bg="white",
            width=25
        )
        long_max = tk.DoubleVar()
        LONG_MAX = long_min.get()
        long_max.set = float
        longmax = tk.Label(gui, text="Maximum longitude: ")
        longmax_txt = tk.Entry(
            gui,
            textvariable=long_max,
            fg="blue",
            bg="white",
            width=25
        )
        longmin.pack()
        longmin_txt.pack()
        longmax.pack()
        longmax_txt.pack()
        # LONG
        lat_min = tk.DoubleVar()
        LAT_MIN = lat_min.get()
        lat_min.set = float
        latmin = tk.Label(gui, text="Minimum latitude: ")
        latmin_txt = tk.Entry(
            gui,
            textvariable=lat_min,
            fg="green",
            bg="white",
            width=25
        )

        lat_max = tk.DoubleVar()
        LAT_MAX = lat_max.get()
        lat_max.set = float
        latmax = tk.Label(gui, text="Maximum latitude: ")
        latmax_txt = tk.Entry(
            gui,
            textvariable=lat_max,
            fg="green",
            bg="white",
            width=25
        )
        latmin.pack()
        latmin_txt.pack()
        latmax.pack()
        latmax_txt.pack()
        # LAT
        space2 = tk.Label(text="______________________________________________________________________________")
        space2.pack()

        # Nlags
        def changetxt():
            if on_off_exval['text'] == 'Exact value = OFF':
                on_off_exval['text'] = 'Exact value = ON'
            else:
                on_off_exval['text'] = 'Exact value = OFF'
                # changes the text in the exact value box depending on whether it was clicked or not.
        def boolex():
            while on_off_exval['text'] == 'Exact value = OFF':
                EXV = 'False'
            while on_off_exval['text'] == 'Exact value = ON':
                EXV = 'True'

        on_off_exval = tk.Button(
            text='Exact value = OFF',
            fg="black",
            bg="white",
            activebackground="blue",
            width=15,
            command=changetxt
        )
        on_off_exval.pack(pady=5)
        # booleans (weight and exact values)
        def changetxt2():
            if weights['text'] == 'Weights = OFF':
                weights['text'] = 'Weights = ON'
            else:
                weights['text'] = 'Weights = OFF'
                # changes the text in the exact value box depending on whether it was clicked or not.

        def boolweight():
            while weights['text'] == 'Weights = OFF':
                WHEY = 'False'
            while weights['text'] == 'Weights = ON':
                WHEY = 'True'

        weights = tk.Button(
            text='Weights = OFF',
            fg="black",
            bg="white",
            activebackground="blue",
            width=15,
            command=changetxt2
        )
        weights.pack(pady=5)


    main()
    gui.mainloop()



    # TODO, Have user enter path to the csv files, remeber to fix path in conc function
    # TODO, Add a user defined domain and range, cause shape file D-R varies wildley, maybe can auto in future.
    # setting file path, the user will do this later
    direct = '/home/pabritt/Krig'

    # TODO: FRONTEND: HAVE USER DEFINE OUTPUT FILE LOCATION AND NAME
    # outputfile stuff

    # reporojecting the shapefile
    # TODO: FRONTEND: have user input mask shapefile
    shape = Repo.repo()

    # concatinating and labeling the data
    df = Conc.conc(direct)

    # TODO: ADD CLEANNG ALGORITHM
    # cleaning algorithm
    # returns chosen dataframe

    # writing shape file
    Write_Shape.write_file(df)

    #### START OF KRIGING ####
    # with multiprocessing.Pool() as pool:
    # for result in pool.map(Kriging.kriging,df,shape):
    # z,ss,gridx,gridy= result
    # we pass shape to mask the interpolation
    z, ss, gridx, gridy = Kriging.kriging(df, shape)

    # writting the tiff function, the grid is passed to define resolution, data frame defines domain and range,z for values
    Write_Tiff.write_file(z, gridx, gridy)

    # clipping the tif here, using the cookie cutter and outputted tiff under write tiff function.
    Clip.clip()
