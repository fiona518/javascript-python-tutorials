#!/usr/bin/python3
from tkinter import *

top = Tk()
top.geometry('140x100')

lbl = Label(top, text="A list of favourite countries...")

listbox = Listbox(top)

listbox.insert(1, "India")
listbox.insert(2, "USA")
listbox.insert(3, "Japan")
listbox.insert(4, "Australia")

btn = Button(top, text="delete", command= lambda listbox=listbox: listbox.delete(ANCHOR))

lbl.pack()
listbox.pack()
btn.pack()

top.mainloop()