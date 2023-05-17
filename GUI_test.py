import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
import Main

gui = Tk(className="-Field Interpolation Tool [FIT]-")
gui.geometry("340x740")


def maingui():
    def csvfile():
        entry_one.delete(0, END)
        csv_path = filedialog.askopenfilename(parent=gui, title="Choose a file.")
        csv_path_true = tk.StringVar()
        if csv_path:
            csv_path_true = os.path.abspath(csv_path)
        csv_copy = csv_path_true
        # csv_path has the true file path
        csv_copy = csv_copy.__str__()
        notcsv = "File must be a '.csv' or '.shp' file!"
        # retrieves the file
        csv_copy2 = csv_copy.replace("<_io.TextIOWrapper name='", '').replace("' mode='r' encoding='cp1252'>", '')
        if '.csv' or '.shp' in csv_copy2:
            entry_one.insert(
                0,
                csv_copy2
            )
            # validates the file type
        else:
            entry_one.insert(
                0,
                notcsv
            )

    CSV = tk.StringVar(gui)
    inpone = tk.Label(text="Input .csv/.shp file(s) or folder.")
    entry_one = tk.Entry(
        textvariable=CSV,
        fg="red",
        bg="white",
        width=40
    )
    csvbutton = tk.Button(
        text="Open File",
        width=7,
        command=csvfile
    )

    csvwarn = tk.Label(
        text=".CSV file must be in X, Y, Z format (Lat/Long/Depth)",
        fg="Red"
    )

    utmval = tk.BooleanVar(gui)

    def dirt():
        if utmsel['text'] == 'NO':
            utmsel['text'] = 'YES'
            utmval.set(True)
            # sends out a value for true
            # true means they want the dirty values
        else:
            utmsel['text'] = 'NO'
            utmval.set(False)
            # false means they do not want the dirty values

    utmlab = tk.Label(text="Is the .csv in UTM coordinates?")
    utmsel = tk.Button(
        text="NO",
        command=dirt
    )

    utmletterval = tk.StringVar(gui)

    utmletter = tk.Label(text="Enter the zone designator:")
    utmletent = tk.Entry(
        textvariable=utmletterval,
        width=4
    )

    utmnumberval = tk.IntVar(gui)

    utmnumber = tk.Label(text="Enter the zone number:")
    utmnument = tk.Entry(
        textvariable=utmnumberval,
        width=4
    )

    # put csvs here

    def shpfile():
        entry_two.delete(0, END)
        shp_path = filedialog.askopenfile()
        shp_copy = shp_path
        # shp_path is the true file path
        # TODO have the gui return this instead of the string
        shp_copy = shp_copy.__str__()
        # retrieves the file
        shp_copy2 = shp_copy.replace("<_io.TextIOWrapper name='", '').replace("' mode='r' encoding='cp1252'>", '')
        entry_two.insert(
            0,
            shp_copy2
        )

    SHP = tk.StringVar(gui)
    inp_two = tk.Label(text="Input .shp file(s) or folder.")
    entry_two = tk.Entry(
        textvariable=SHP,
        fg="red",
        bg="white",
        width=40
    )
    shpbutton = tk.Button(
        text="Open File",
        width=7,
        command=shpfile
    )
    # put OG shapefiles
    ML = tk.BooleanVar(gui)

    seatext = tk.Label(text="Enter the mean sea level:")

    seaval = tk.DoubleVar(gui)

    seaent = tk.Entry(
        textvariable=seaval,
        fg='red'
    )

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
        state="disabled",
        command=skynet
    )
    # Machine learning
    # TODO should have it so that this will run and suggest the best settings for the kriging
    MLwarning1 = tk.Label(
        text="WARNING: Machine Learning finds the best fit settings.",
        fg="red"
    )
    MLwarning2 = tk.Label(
        text="This will take several minutes to run.",
        fg="red"
    )

    # TODO disable the ML button when the ML button is off and/or there is no .csv file present

    terminator = tk.Button(
        text="Run Machine Learning",
        bg="Grey",
        fg="White",
        width=18,
        state="disabled"

        # command=lambda: machinelearning(CSV.get(), ML.get())
    )
    # button to run ML

    # TODO this should freeze the program while ML runs, a pop-up box should appear while it runs, then says when done
    space0 = tk.Label(text="______________________________________________________________________________")
    space0.pack()
    # makes a line to separate the GUI (just for visuals)
    inpone.pack()
    entry_one.pack()
    csvbutton.pack()
    csvwarn.pack()
    utmlab.pack()
    utmsel.pack()
    utmletter.pack()
    utmletent.pack()
    utmnumber.pack()
    utmnument.pack()
    inp_two.pack()
    entry_two.pack()
    shpbutton.pack()
    seatext.pack()
    seaent.pack()
    mlbutton.pack(pady=5)
    MLwarning1.pack()
    MLwarning2.pack()
    terminator.pack()
    space1 = tk.Label(text="______________________________________________________________________________")
    space1.pack()

    # makes a line to separate the GUI (just for visuals)

    def lagtype():
        if lag_opt == "6":
            lags_true = "6"
            return lags_true
        elif lag_opt == "8":
            lags_true = "8"
            return lags_true
        elif lag_opt == "10":
            lags_true = "10"
            return lags_true
        elif lag_opt == "15":
            lags_true = "15"
            return lags_true
        elif lag_opt == "20":
            lags_true = "20"
            return lags_true
        else:
            return

    lags_txt = tk.Label(text="Enter the number of lags for the Variogram:")
    lag_opt = ["6", "8", "10", "15", "20"]
    lags_true = StringVar(gui)
    lags_true.set("6")
    lags_ent = OptionMenu(gui, lags_true, *lag_opt, command=lagtype())
    lags_txt.pack()
    lags_true.get()
    lags_ent.pack()

    # Nlags
    EXV = BooleanVar(gui)

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

    # booleans (exact value)

    dropdown = tk.StringVar(gui)

    def type1():
        if options == "linear":
            dropdown1 = "linear"
        elif options == "power":
            dropdown1 = "power"
        elif options == "spherical":
            dropdown1 = "spherical"
        elif options == "exponential":
            dropdown1 = "exponential"
        elif options == "gaussian":
            dropdown1 = "gaussian"
        else:
            return

        # returns a string of characters for the selected kriging type

    options = ["linear", "power", "spherical", "exponential", "gaussian"]
    dropdown = StringVar(gui)
    dropdown.set("linear")
    drop = OptionMenu(gui, dropdown, *options, command=type1())
    dropdown.get()
    drop.pack(pady=5)

    # dropdown menu

    dirtval = BooleanVar(gui)

    def dirt():
        if dirtysel['text'] == 'YES':
            dirtysel['text'] = 'NO'
            dirtval.set(True)
            # sends out a value for true
            # true means they want the dirty values
        else:
            dirtysel['text'] = 'YES'
            dirtval.set(False)
            # false means they do not want the dirty values

    dirtylab = tk.Label(text="Do you want to keep the dirty values?")
    dirtysel = tk.Button(
        text="YES",
        command=dirt
    )
    dirtylab.pack()
    dirtysel.pack()

    space0 = tk.Label(text="______________________________________________________________________________")
    space0.pack()

    runbutton = tk.Button(
        gui,
        text="Run",
        bg="Red",
        fg="White",
        activebackground="Green",
        width=10,
        command=lambda: Main.dropSEQ(CSV.get(), utmval.get(), utmletterval.get(), utmnumberval.get(), SHP.get(), seaval.get(),
                                     ML.get(), lags_true.get(), EXV.get(), dropdown.get(), dirtval.get())
    )
    # just creates a button to click when the program is ready to run, then sends values to main
    runbutton.pack(pady=3)


maingui()
gui.mainloop()

# ah yes, long file time
