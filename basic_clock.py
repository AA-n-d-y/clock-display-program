# Program for a Clock Displaying the Current Time
#
#
#################################################


### Importing necessary libraries

import tkinter as tk
from tkinter import Label, Frame, StringVar, Button
from time import strftime


### Functions

def currentTime():
    global text_line
    text_line = ""
    timeCurrent = strftime("%I:%M:%S %p")
    text_line += timeCurrent
    timeDisplay.set(text_line)
    alarmText.after(1000, currentTime)


### Creating the window

window = tk.Tk()
window.title("Clock")
window.geometry("900x400")
window.configure(bg = "black")


### Variables

timeDisplay = StringVar()


### Labels

alarmTitle = Label(window, height = 1, font = ("Roboto", 22), fg = "turquoise", \
        text = "Clock", bg = "black")
alarmTitle.pack()

alarmText = Label(window, bg = "black", width = 26, height = 2, font = ("Roboto", 100), \
        fg = "turquoise", textvariable = timeDisplay)
alarmText.pack(anchor = "center")


### Calling the time function

currentTime()


### Running the window

window.mainloop()



### End of program