from tkinter import *


window = Tk()
window.minsize(width=400, height=300)

label = Label(text="I Am A Label", font=("Arial", 24, "bold"))
label.pack()


def button_clicked():
    label["text"] = "Hello"
    label.pack()

button = Button(text="Click Me", command=button_clicked)
button.pack()

window.mainloop()
