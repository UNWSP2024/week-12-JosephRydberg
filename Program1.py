#MPG Joseph Rydberg 11/18/24
import tkinter
from tkinter import Entry, Button, Label

window = tkinter.Tk()

miles = tkinter.IntVar()
gallons = tkinter.IntVar()

def mpg():

    window.title("MPG Calculator")

    totalMilesEntry = Entry(window, textvariable=miles)
    milesLabel = Label(window, text="Total Miles")
    tankSizeEntry = Entry(window, textvariable=gallons)
    gallonsLabel = Label(window, text="Total Gallons")

    def find_total():
        total = miles.get() / gallons.get()
        milesGallon = Label(window, text=str(total) + "Miles/Gallon")
        milesGallon.pack()

    calculate = Button(window, text="Calculate MPG", command=find_total)

    totalMilesEntry.pack()
    milesLabel.pack()
    tankSizeEntry.pack()
    gallonsLabel.pack()
    calculate.pack()
    window.mainloop()

mpg()