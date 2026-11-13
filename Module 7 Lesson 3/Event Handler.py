# Import Libraries
from tkinter import *

#Create Window

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

#Event Handler
def handle_keypress(event):
    print(event.char)
#Keypress event
window.bind("<Key>", handle_keypress)
#Event Handler
def handle_click(event):
    print("\nThe button has been pressed")

button = Button(text="Click me!")
button.pack()
#Bind click event
button.bind("<Button-1>", handle_click)
#GUI loop
window.mainloop()