#Import Libraries
from tkinter import *
from tkinter import messagebox

#Setup Window
root = Tk()
root.geometry("300x500")

#Warning Message
def msg():
    messagebox.showwarning("Stop!", "You got a virus!")

#Adding button widget to window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=100, y=100)

#Main event loop
root.mainloop()