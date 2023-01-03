import tkinter as tk
from tkinter import *
# import GUI_test

# from tkinter import filedialog

# will need to use filedialog since the GUI would be pulling the output file location for the user
# it's not entirely useless...I didn't say that, you did
outgui = Tk(className="-GENEX GUI tool")
outgui.geometry("200x200")


def guistuff():
    outfiletxt = tk.Label(text="Location of file:")
    outfile = tk.Entry(
        outgui,
        fg="green",
        width=35,
        state='disabled'
        # disabled to ensure the user cannot change the contents of the box, they can only copy the file path
        # TODO will have to input the file/file location into the entry box
    )

    quitbutton = tk.Button(
        text="QUIT",
        bg="red",
        fg="white",
        width=10,
        command=outgui.quit
    )

    runagain = tk.Button(
        text="RUN AGAIN?",
        bg="green",
        fg="white",
        width=10
        # TODO the button will have to reopen the original GUI and restart the program for new entries
    )
    outfiletxt.pack()
    outfile.pack()
    runagain.pack()
    quitbutton.pack()


guistuff()
outgui.mainloop()
