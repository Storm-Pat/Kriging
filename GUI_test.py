import tkinter as tk
from tkinter import *
import os

# TODO create directory for import files to go
# TODO create checks for the lat long to ensure the entered values are, in fact, values and not a bunch of letters
# TODO create another GUI that this GUI points to after interpolation displaying all available data
# TODO create a stop point that points to graphed data
gui = Tk(className='GENEX script-main input')
gui.geometry("340x520")


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
    # choosing whether or not to use specific lat and long values

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

    # makes a line to seperate the GUI (just for visuals)

    # Nlags
    def changetxt():
        if on_off_exval['text'] == 'Exact value = OFF':
            on_off_exval['text'] = 'Exact value = ON'
            while on_off_exval['text'] == 'Exact value = ON':
                EXV = 'True'
                return EXV == 1
            # sends out a boolean value for true
        else:
            on_off_exval['text'] = 'Exact value = OFF'
            while on_off_exval['text'] == 'Exact value = OFF':
                EXV = 'False'
                return EXV == 0
            # senmds out a boolean value for false
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
                WHEY = 'True'
                return WHEY == 1
        else:
            weights['text'] = 'Weights = OFF'
            while weights['text'] == 'Weights = OFF':
                WHEY = 'False'
                return WHEY == 0
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
            dropdown = 1
            return dropdown
        elif options == "Power":
            dropdown = 2
            return dropdown
        elif options == "Spherical":
            dropdown = 3
            return dropdown
        elif options == "Exponential":
            dropdown = 4
            return dropdown
        elif options == "Gaussian":
            dropdown = 5
            return dropdown
        else:
            return

    def show():
        label.config(text=clicked.get())
        dropdown = tk.StringVar()
        DRPMNU = dropdown.get()
        dropdown.set = str
        return DRPMNU

    # returns an integer value for dropdown menu

    options = ["Linear", "Power", "Spherical", "Exponential", "Gaussian"]
    clicked = StringVar()
    clicked.set("Linear")
    drop = OptionMenu(gui, clicked, *options)
    clicked.get()
    command = type1
    drop.pack()
    # dropdown menu

    label = Label(gui, text=" ")
    label.pack()

    runbutton = tk.Button(
        text="Run",
        bg="Red",
        fg="White",
        activebackground="Green",
        width=10
    )
    runbutton.pack()
    # just creates a button to click when the program is ready to run

    # return CSV, SHP, LONG_MIN, LONG_MAX, LAT_MIN, LAT_MAX


# returns all the values received from the main function, the smaller functions inside "maingui" return their own value


maingui()
gui.mainloop()
