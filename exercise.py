from tkinter import *

root =  Tk()
root.geometry("200x200")

spin = Spinbox(root, from_=0, to=25)
spin.pack()

root.mainloop()