from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")

# messagebox.showinfo("information, information")
# messagebox.showwarning('warning', 'Warning')
# messagebox.showerror("error",  "Error")
# messagebox.askquestion("Confirm", "Are you sure?")
# messagebox.askokcancel("Redirect", "Redirecting you to www.javatpoint.com")
# messagebox.askyesno("Application", "Got it?")
messagebox.askretrycancel("Application", "try again?")

top.mainloop()