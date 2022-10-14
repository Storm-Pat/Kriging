import tkinter as tk
from tkinter import *
from tkinter import filedialog


# TODO create directory for import files to go
# TODO create checks for the lat long to ensure the entered values are, in fact, values and not a bunch of letters
# TODO create another GUI that this GUI points to after interpolation displaying all available data
# TODO create a stop point that points to graphed data

def guidrop(CSV, SHP, LONG_MIN, LONG_MAX, LAT_MIN, LAT_MAX, dropdown, ML, EXV, WHEY, lags_ent):
    print(CSV)
    print(SHP)
    # the if statements are "proof of concept"
    if LONG_MIN != 0.0:
        print(LONG_MIN)
    if LONG_MAX != 0.0:
        print(LONG_MAX)
    if LAT_MIN != 0.0:
        print(LAT_MIN)
    if LAT_MAX != 0.0:
        print(LAT_MAX)
        # the GUI will return "0.0" for LAT/LONG values if the user chooses to use the values in their data,
        # this will stop the program from setting the value of LAT/LONG to 0.0 and generating an incorrect krige.
    print(lags_ent)
    print(EXV)
    print(WHEY)
    print(dropdown)
    print(ML)
    # This is in the exact format of how the GUI entries are set up, with CSV input being first and ML being the last
    # input

    # this will be implemented into the main kriging function eventually, passes the values received by the GUI to
    # back-end function.


gui = Tk(className="-GENEX GUI tool-")
gui.geometry("340x640")


def maingui():

    def csvfile():
        csv_path = filedialog.askopenfile()
        print(csv_path)
        entry_one.insert(
            0,
            csv_path
        )

    CSV = tk.StringVar()
    inpone = tk.Label(text="Input .csv file(s) or folder.")
    entry_one = tk.Entry(
        gui,
        textvariable=CSV,
        fg="red",
        bg="white",
        width=40
    )
    csvbutton = tk.Button(
        width=6,
        command=csvfile
    )
    # put csvs here

    def shpfile():
        shp_path = filedialog.askopenfile()
        entry_two.insert(
            0,
            shp_path
        )

    SHP = tk.StringVar()
    inp_two = tk.Label(text="Input .shp file(s) or folder.")
    entry_two = tk.Entry(
        gui,
        textvariable=SHP,
        fg="red",
        bg="white",
        width=40
    )
    shpbutton = tk.Button(
        width=6,
        command=shpfile
    )
    # put og shapes
    space0 = tk.Label(text="______________________________________________________________________________")
    space0.pack()
    # makes a line to seperate the GUI (just for visuals)
    inpone.pack()
    entry_one.pack()
    csvbutton.pack()
    inp_two.pack()
    entry_two.pack()
    shpbutton.pack()
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
                # changes the LAT/LONG from modifiable to disabled text box

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

    LONG_MIN = tk.DoubleVar()
    # retrieves minimum longitude as float
    longmin = tk.Label(gui, text="Minimum longitude: ")
    longmin_txt = tk.Entry(
        gui,
        textvariable=LONG_MIN,
        fg="blue",
        bg="white",
        width=25
    )
    LONG_MAX = tk.DoubleVar()
    # retrieves maximum longitude as float
    longmax = tk.Label(gui, text="Maximum longitude: ")
    longmax_txt = tk.Entry(
        gui,
        textvariable=LONG_MAX,
        fg="blue",
        bg="white",
        width=25
    )
    # LONG
    LAT_MIN = tk.DoubleVar()
    # retrieves minimum latitude as float
    latmin = tk.Label(gui, text="Minimum latitude: ")
    latmin_txt = tk.Entry(
        gui,
        textvariable=LAT_MIN,
        fg="green",
        bg="white",
        width=25
    )

    LAT_MAX = tk.DoubleVar()
    # retrieves maximum latitude as float
    latmax = tk.Label(gui, text="Maximum latitude: ")
    latmax_txt = tk.Entry(
        gui,
        textvariable=LAT_MAX,
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

    lags_ent = IntVar()

    lags_txt = tk.Label(text="Enter the number of lags for the Variogram:")
    lags_ent = tk.Entry(
        fg='black',
        width=10
    )
    lags_txt.pack()
    lags_ent.pack()

    # Nlags
    EXV = BooleanVar()

    def changetxt():
        if on_off_exval['text'] == 'Exact value = OFF':
            on_off_exval['text'] = 'Exact value = ON'
            EXV.set(True)
            # sends out a value for true (boolean?)
        else:
            on_off_exval['text'] = 'Exact value = OFF'
            EXV.set(False)
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

    WHEY = BooleanVar()

    def changetxt2():
        if weights['text'] == 'Weights = OFF':
            weights['text'] = 'Weights = ON'
            WHEY.set(True)
        else:
            weights['text'] = 'Weights = OFF'
            WHEY.set(False)

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

    dropdown = tk.StringVar()

    def type1():
        if options == "Linear":
            dropdown = "linear"
            return dropdown == "linear"
        elif options == "Power":
            dropdown = "power"
            return dropdown == "power"
        elif options == "Spherical":
            dropdown = "spherical"
            return dropdown == "spherical"
        elif options == "Exponential":
            dropdown = "exponential"
            return dropdown == "exponential"
        elif options == "Gaussian":
            dropdown = "gaussian"
            return dropdown == "gaussian"
        else:
            return

        # returns a string of characters for the selected kriging type

    options = ["Linear", "Power", "Spherical", "Exponential", "Gaussian"]
    dropdown = StringVar()
    dropdown.set("Linear")
    drop = OptionMenu(gui, dropdown, *options, command=type1())
    dropdown.get()
    drop.pack(pady=5)

    # dropdown menu

    ML = tk.BooleanVar()

    def skynet():
        if mlbutton["text"] == "Machine Learning = OFF":
            mlbutton["text"] = "Machine Learning = ON"
            ML.set(True)
        else:
            mlbutton["text"] = "Machine Learning = OFF"
            ML.set(False)

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
        width=10,
        command=lambda: guidrop(CSV.get(), SHP.get(), LONG_MIN.get(), LONG_MAX.get(), LAT_MIN.get(), LAT_MAX.get(),
                                dropdown.get(), ML.get(), EXV.get(), WHEY.get(), lags_ent.get())
    )
    runbutton.pack(pady=3)
    # just creates a button to click when the program is ready to run, then sends values to main


maingui()
gui.mainloop()
