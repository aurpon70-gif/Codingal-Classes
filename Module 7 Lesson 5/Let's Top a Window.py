# Import Libraries
from tkinter import *

#Setting up window
root = Tk()
root.geometry("400x300")
root.title("main")

#Function to open new window
def topwin():
    #Setting up top window
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")

    #Adding a label widget to Top Window
    l2 = Label(top, text="this is the toplevel window")
    l2.pack()

    top.mainloop()

#Adding a label and button widget
l = Label(root, text="this is the root window")
btn = Button(root, text="click here for another window", command=topwin)

l.pack()
btn.pack()

root.mainloop()