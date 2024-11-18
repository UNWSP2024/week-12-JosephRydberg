import tkinter as tk
from tkinter import Entry, Button, Label

window = tk.Tk()
window.title("Hour rates")

def rates():

    mins = tk.IntVar()

    costTotal = Label(window, text="Cost: $0")

    def day_hours():
        cost = mins.get() * 0.02
        costTotal.config(text="Cost: $" + str(cost))
    def night_hours():
        cost = mins.get() * 0.12
        costTotal.config(text="Cost: $" + str(cost))
    def off_hours():
        cost = mins.get() * 0.05
        costTotal.config(text="Cost: $" + str(cost))

    day = Button(window, text="Calculate Day Call", command= day_hours)
    night = Button(window, text="Calculate Night Call", command= night_hours)
    offPeak = Button(window, text="Calculate Off Hours Call", command= off_hours)
    minLabel = Label(window, text="Enter Call Length In Minutes")
    minutes = Entry(window, textvariable=mins)

    day.pack()
    night.pack()
    offPeak.pack()
    minLabel.pack()
    minutes.pack()
    costTotal.pack()

    window.mainloop()

rates()