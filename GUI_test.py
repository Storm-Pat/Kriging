import tkinter as tk
from tkinter import *

# TODO create directory for import files to go
# TODO create checks for the lat long to ensure the entered values are, in fact, values and not a bunch of letters
# TODO create another GUI that this GUI points to after interpolation displaying all available data
# TODO create a stop point that points to graphed data

gui = Tk(className='GENEX script-main input')
gui.geometry("340x600")


def maingui():
    csv_f = tk.StringVar()
    CSV = csv_f.get()
    csv_f.set = str
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
    shp_f.set = str
    inp_two = tk.Label(text="Input .shp file(s) or folder.")
    entry_two = tk.Entry(
        gui,
        textvariable=shp_f,
        fg="red",
        bg="white",
        width=40
    )
    # put og shapes
    space0 = tk.Label(text="______________________________________________________________________________")
    space0.pack()
    # makes a line to seperate the GUI (just for visuals)
    inpone.pack()
    entry_one.pack()
    inp_two.pack()
    entry_two.pack()
    space1 = tk.Label(text="______________________________________________________________________________")
    space1.pack()

    # makes a line to seperate the GUI (just for visuals)
    def changelabel():
        if buttonchoice['text'] == 'No':
            buttonchoice['text'] = 'Yes'
            if buttonchoice['text'] == 'Yes':
                longmin_txt.config(state='normal')
                longmax_txt.config(state='normal')
                latmin_txt.config(state='normal')
                latmax_txt.config(state='normal')
        else:
            buttonchoice['text'] = 'No'
            if buttonchoice['text'] == 'No':
                longmin_txt.config(state='disabled')
                longmax_txt.config(state='disabled')
                latmin_txt.config(state='disabled')
                latmax_txt.config(state='disabled')

    rangechoice = tk.Label(gui, text="Do you want to use specific domain/range?")
    buttonchoice = tk.Button(
        gui,
        text="Yes",
        fg="black",
        bg="white",
        activebackground="green",
        width=6,
        command=changelabel
    )

    long_min = tk.DoubleVar()
    LONG_MIN = long_min.get()
    long_min.set = DoubleVar
    # retrieves minimum longitude as float
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
    long_max.set = DoubleVar
    # retrieves maximum longitude as float
    longmax = tk.Label(gui, text="Maximum longitude: ")
    longmax_txt = tk.Entry(
        gui,
        textvariable=long_max,
        fg="blue",
        bg="white",
        width=25
    )
    # LONG
    lat_min = tk.DoubleVar()
    LAT_MIN = lat_min.get()
    lat_min.set = DoubleVar
    # retrieves minimum latitude as float
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
    lat_max.set = DoubleVar
    # retrieves maximum latitude as float
    latmax = tk.Label(gui, text="Maximum latitude: ")
    latmax_txt = tk.Entry(
        gui,
        textvariable=lat_max,
        fg="green",
        bg="white",
        width=25
    )

    rangechoice.pack()
    buttonchoice.pack()
    # choosing whether to use specific lat and long values

    longmin.pack()
    longmin_txt.pack()
    longmax.pack()
    longmax_txt.pack()

    latmin.pack()
    latmin_txt.pack()
    latmax.pack()
    latmax_txt.pack()
    # LAT

    space2 = tk.Label(text="______________________________________________________________________________")
    space2.pack()

    # makes a line to separate the GUI (just for visuals)

    lags_txt = tk.Label(text="Enter the number of lags for the Variogram:")
    lags_ent = tk.Entry(
        fg='black',
        width=10
    )
    lags_txt.pack()
    lags_ent.pack()

    # Nlags

    def changetxt():
        if on_off_exval['text'] == 'Exact value = OFF':
            on_off_exval['text'] = 'Exact value = ON'
            while on_off_exval['text'] == 'Exact value = ON':
                EXV = 'True'
                return EXV == True
            # sends out a value for true (boolean?)
        else:
            on_off_exval['text'] = 'Exact value = OFF'
            while on_off_exval['text'] == 'Exact value = OFF':
                EXV = 'False'
                return EXV == False
            # sends out a value for false (boolean?)
        # changes the text in the exact value box depending on whether it was clicked or not.

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
            while weights['text'] == 'Weights = ON':
                WHEY = 1
                return WHEY == True
        else:
            weights['text'] = 'Weights = OFF'
            while weights['text'] == 'Weights = OFF':
                WHEY = 0
                return WHEY == False
            # changes the text in the exact value box depending on whether it was clicked or not.

    weights = tk.Button(
        text='Weights = OFF',
        fg="black",
        bg="white",
        activebackground="blue",
        width=15,
        command=changetxt2
    )
    weights.pack(pady=5)

    def type1():
        if options == "Linear":
            dropdown = 'linear'
            return dropdown
        elif options == "Power":
            dropdown = 'power'
            return dropdown
        elif options == "Spherical":
            dropdown = 'spherical'
            return dropdown
        elif options == "Exponential":
            dropdown = 'exponential'
            return dropdown
        elif options == "Gaussian":
            dropdown = 'gaussian'
            return dropdown
        else:
            return

    options = ["Linear", "Power", "Spherical", "Exponential", "Gaussian"]
    clicked = StringVar()
    clicked.set("Linear")
    drop = OptionMenu(gui, clicked, *options)
    clicked.get()
    command = type1
    drop.pack(pady=5)

    # dropdown menu

    def skynet():
        if mlbutton['text'] == 'Machine Learning = OFF':
            mlbutton['text'] = 'Machine Learning = ON'
        else:
            mlbutton['text'] = 'Machine Learning = OFF'
        if mlbutton['text'] == 'Machine Learning = ON':
            ML = 1
            return ML == True
        elif mlbutton['text'] == 'Machine Learning = OFF':
            ML = 0
            return ML == False
        else:
            return

    mlbutton = tk.Button(
        text="Machine Learning = OFF",
        bg="white",
        fg='black',
        activebackground='purple',
        width=19,
        command=skynet
    )

    mlbutton.pack(pady=5)

    runbutton = tk.Button(
        text="Run",
        bg="Red",
        fg="White",
        activebackground="Green",
        width=10
    )
    runbutton.pack(pady=3)
    # just creates a button to click when the program is ready to run

    # return CSV, SHP, LONG_MIN, LONG_MAX, LAT_MIN, LAT_MAX


# returns all the values received from the main function, the smaller functions inside "maingui" return their own value


maingui()
gui.mainloop()
