import tkinter as tk
from tkinter import *
from tkinter import filedialog

# will need to use filedialog since the GUI would be pulling the output file location for the user
# it's not entirely useless...I didn't say that, you did
outgui = Tk(className="-GENEX GUI tool")
outgui.geometry("400x400")


def guistuff():
    outfiletxt = tk.Label(text="Location of file:")
    outfile = tk.Entry(
        outgui,
        fg="green",
        width=35,
        state='disabled'
        # disabled to ensure the user cannot change the contents of the box, they can only copy the file path
    )
    # TODO will need a button asking if they want to run the kriging again
    # TODO the button will have to reopen the original GUI and restart the program for new entries
    # TODO will also need a button asking if the user would like to quit the program
    outfiletxt.pack()
    outfile.pack()


guistuff()
outgui.mainloop()
