import tkinter
from tkinter import *

root = Tk()

t = tkinter.Text(root)
t.insert(INSERT, "Texte 1")
t.grid(row=0, column=0)

p = tkinter.Text(root)
p.insert(INSERT, "Texte 2")
p.grid(row=0, column=1)

root.mainloop()