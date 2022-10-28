import tkinter as tk
from tkinter import *
from tkinter import filedialog

outgui = Tk(className="-GENEX GUI tool")
outgui.geometry("400x400")

def guistuff():
    outfiletxt = tk.Label(text="Location of file:")
    outfile = tk.Entry(
        outgui,
        fg="green",
        width=35,
        state='disabled'
    )
    outfiletxt.pack()
    outfile.pack()


guistuff()
outgui.mainloop()
