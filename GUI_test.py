import tkinter as tk
from tkinter import *
from tkinter import filedialog


# TODO create directory for import files to go

def guidrop(CSV, SHP, ML, lags_true, EXV, dropdown, dirtval):
    print(CSV)
    print(SHP)
    print("machines", ML)
    print("number of lags", lags_true)
    print("this is dirt", dirtval)
    print("exact value", EXV)
    print("krig type", dropdown)
    # This is in the exact format of how the GUI entries are set up, with CSV input being first and ML being the last
    # input

    # this will be implemented into the main kriging function eventually, passes the values received by the GUI to
    # back-end function.

def machinelearning(CSV, ML):
    print(CSV)
    print(ML)



gui = Tk(className="-GENEX GUI tool-")
gui.geometry("340x660")


def maingui():
    def csvfile():
        entry_one.delete(0, END)
        csv_path = filedialog.askopenfile()
        csv_copy = csv_path
        csv_copy = csv_copy.__str__()
        notcsv = "File must be a '.csv' file!"
        # retrieves the file
        csv_copy2 = csv_copy.replace("<_io.TextIOWrapper name='", '').replace("' mode='r' encoding='cp1252'>", '')
        if '.csv' in csv_copy2:
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
        text="Open File",
        width=7,
        command=csvfile
    )

    # put csvs here

    def shpfile():
        entry_two.delete(0, END)
        shp_path = filedialog.askopenfile()
        shp_copy = shp_path
        shp_copy = shp_copy.__str__()
        # retrieves the file
        shp_copy2 = shp_copy.replace("<_io.TextIOWrapper name='", '').replace("' mode='r' encoding='cp1252'>", '')
        entry_two.insert(
            0,
            shp_copy2
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
        text="Open File",
        width=7,
        command=shpfile
    )
    # put OG shapefiles
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

    def termbuttondecide():
        a = CSV.get() # string variable
        b = ML.get() # boolean variable
        # TODO should find a way to make a boolean variable for the file instead of checking for a string
        # TODO disable the ML button when the ML button is off and/or there is no .csv file present


    terminator = tk.Button(
        text="Run Machine Learning",
        bg="Red",
        fg="White",
        width=18,
        state='disabled',
        command=termbuttondecide
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
    inp_two.pack()
    entry_two.pack()
    shpbutton.pack()
    mlbutton.pack(pady=5)
    MLwarning1.pack()
    MLwarning2.pack()
    terminator.pack()
    space1 = tk.Label(text="______________________________________________________________________________")
    space1.pack()
    #
    # # makes a line to separate the GUI (just for visuals)
    # def changelabel():
    #     if buttonchoice['text'] == 'No':
    #         buttonchoice['text'] = 'Yes'
    #         if buttonchoice['text'] == 'Yes':
    #             longmin_txt.config(state='normal')
    #             longmax_txt.config(state='normal')
    #             latmin_txt.config(state='normal')
    #             latmax_txt.config(state='normal')
    #     else:
    #         buttonchoice['text'] = 'No'
    #         if buttonchoice['text'] == 'No':
    #             longmin_txt.config(state='disabled')
    #             longmax_txt.config(state='disabled')
    #             latmin_txt.config(state='disabled')
    #             latmax_txt.config(state='disabled')
    #             # changes the LAT/LONG from modifiable to disabled text box
    #
    # rangechoice = tk.Label(gui, text="Do you want to use specific domain/range?")
    # buttonchoice = tk.Button(
    #     gui,
    #     text="No",
    #     fg="black",
    #     bg="white",
    #     activebackground="green",
    #     width=6,
    #     command=changelabel
    # )
    #
    # LONG_MIN = tk.DoubleVar()
    # # retrieves minimum longitude as float
    # longmin = tk.Label(gui, text="Minimum longitude: ")
    # longmin_txt = tk.Entry(
    #     gui,
    #     textvariable=LONG_MIN,
    #     fg="blue",
    #     bg="white",
    #     state='disabled',
    #     width=25
    # )
    # LONG_MAX = tk.DoubleVar()
    # # retrieves maximum longitude as float
    # longmax = tk.Label(gui, text="Maximum longitude: ")
    # longmax_txt = tk.Entry(
    #     gui,
    #     textvariable=LONG_MAX,
    #     fg="blue",
    #     bg="white",
    #     state='disabled',
    #     width=25
    # )
    # # LONG
    # LAT_MIN = tk.DoubleVar()
    # # retrieves minimum latitude as float
    # latmin = tk.Label(gui, text="Minimum latitude: ")
    # latmin_txt = tk.Entry(
    #     gui,
    #     textvariable=LAT_MIN,
    #     fg="green",
    #     bg="white",
    #     state='disabled',
    #     width=25
    # )
    #
    # LAT_MAX = tk.DoubleVar()
    # # retrieves maximum latitude as float
    # latmax = tk.Label(gui, text="Maximum latitude: ")
    # latmax_txt = tk.Entry(
    #     gui,
    #     textvariable=LAT_MAX,
    #     fg="green",
    #     bg="white",
    #     state='disabled',
    #     width=25
    # )
    #
    # rangechoice.pack()
    # buttonchoice.pack()
    # # choosing whether to use specific lat and long values
    #
    # longmin.pack()
    # longmin_txt.pack()
    # longmax.pack()
    # longmax_txt.pack()
    #
    # latmin.pack()
    # latmin_txt.pack()
    # latmax.pack()
    # latmax_txt.pack()
    # # LAT
    #
    # space2 = tk.Label(text="______________________________________________________________________________")
    # space2.pack()

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
    lags_true = StringVar()
    lags_true.set("6")
    lags_ent = OptionMenu(gui, lags_true, *lag_opt, command=lagtype())
    lags_txt.pack()
    lags_true.get()
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

    # booleans (exact value)

    dropdown = tk.StringVar()

    def type1():
        if options == "Linear":
            dropdown1 = "linear"
            return dropdown1 == "linear"
        elif options == "Power":
            dropdown1 = "power"
            return dropdown1 == "power"
        elif options == "Spherical":
            dropdown1 = "spherical"
            return dropdown1 == "spherical"
        elif options == "Exponential":
            dropdown1 = "exponential"
            return dropdown1 == "exponential"
        elif options == "Gaussian":
            dropdown1 = "gaussian"
            return dropdown1 == "gaussian"
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

    dirtval = BooleanVar()

    def dirt():
        if dirtysel['text'] == 'NO':
            dirtysel['text'] = 'YES'
            dirtval.set(True)
            # sends out a value for true
            # true means they want the dirty values
        else:
            dirtysel['text'] = 'NO'
            dirtval.set(False)
            # false means they do not want the dirty values

    dirtylab = tk.Label(text="Do you want to keep the dirty values?")
    dirtysel = tk.Button(
        text="NO",
        command=dirt
    )
    dirtylab.pack()
    dirtysel.pack()

    space0 = tk.Label(text="______________________________________________________________________________")
    space0.pack()

    runbutton = tk.Button(
        text="Run",
        bg="Red",
        fg="White",
        activebackground="Green",
        width=10,
        command=lambda: guidrop(CSV.get(), SHP.get(), ML.get(), lags_true.get(), EXV.get(), dropdown.get(), dirtval.get())
    )
    # just creates a button to click when the program is ready to run, then sends values to main
    runbutton.pack(pady=3)


maingui()
gui.mainloop()

# ah yes, long file time
