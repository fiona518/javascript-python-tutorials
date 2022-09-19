#!/usr/bin/python3
from tkinter import *

top = Tk()

top.geometry('200x200')

c = Canvas(top, bg="pink", height="200")

arc = c.create_arc((5, 10, 150, 200), start=0, extent=150, fill="white")

c.pack()

top.mainloop()