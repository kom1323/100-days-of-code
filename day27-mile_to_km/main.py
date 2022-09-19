from tkinter import *
from turtle import color
from unittest import TextTestResult


window = Tk()
window.title("Miles To Kilometer Converter")
window.minsize(width=200, height=70)
window.config(padx=10,pady=20)

entry = Entry(width=10)
entry.grid(column=1,row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2,row=0)

label_answer = Label(text="0")
label_answer.grid(column=1,row=1)

label_km = Label(text="Km")
label_km.grid(column=2,row=1)

label = Label(text="is equal to" )
label.grid(column=0, row=1)


def button_func():
    label_answer["text"] = round(float(entry.get()) * 1.609344, 2)

button = Button(text="Calculate", command=button_func)
button.grid(column=1, row=2)


window.mainloop()
