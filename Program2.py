#Automotive Joseph Rydberg 11/18/24
#I tried for 3 hours to get this to work with dictionaries and classes but no matter what
#I couldn't get it to work, so I just went with the bad written version
import tkinter as tk
from tkinter import Entry, Button, Label, Listbox, Checkbutton, StringVar

window = tk.Tk()
window.title("AutoMotive")

s1 = tk.BooleanVar()
s2 = tk.BooleanVar()
s3 = tk.BooleanVar()
s4 = tk.BooleanVar()
s5 = tk.BooleanVar()
s6 = tk.BooleanVar()
s7 = tk.BooleanVar()


def automotive():
    cost = Label(window, text="0")

    def calculate():
        totalCost = 0
        if s1.get():
            totalCost += 30
        if s2.get():
            totalCost += 20
        if s3.get():
            totalCost += 40
        if s4.get():
            totalCost += 100
        if s5.get():
            totalCost += 35
        if s6.get():
            totalCost += 200
        if s7.get():
            totalCost += 20

        cost.config(text="$" + str(totalCost))

    service1 = Checkbutton(window, text="Oil Change - $30.00", variable= s1, command=calculate)
    service2 = Checkbutton(window, text="Lube Job - $20.00", variable= s2, command=calculate)
    service3 = Checkbutton(window, text="Radiator Flush - $40.00", variable= s3, command=calculate)
    service4 = Checkbutton(window, text="Transmission Fluid - $100.00", variable= s4, command=calculate)
    service5 = Checkbutton(window, text="Inspection - $35.00", variable= s5, command=calculate)
    service6 = Checkbutton(window, text="Muffler replacement - $200.00", variable= s6, command=calculate)
    service7 = Checkbutton(window, text="Tire Rotation - $20.00", variable= s7, command=calculate)

    service1.pack()
    service2.pack()
    service3.pack()
    service4.pack()
    service5.pack()
    service6.pack()
    service7.pack()
    cost.pack()

    window.mainloop()

automotive()









