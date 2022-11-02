from re import I
from tkinter import *
import pandas as pd
import time


BACK_CARD_COLOR = "#90C0AD"
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
data = pd.read_csv(r".\day31-flash_card\data\french_words.csv")
curr_word = 0

# ---------------------------- Words changer ------------------------------- #

def next_word():

    
    global curr_word, flip_timer
    
    window.after_cancel(flip_timer)
    curr_word = data.sample(1)
    word_label.config(text=curr_word.iloc[0].at["French"], bg="white", fg="black")
    language_label.config(text="French", bg="white", fg="black")
    canvas.itemconfig(canvas_image, image=front_image)
    flip_timer = window.after(3000, func=display_translation)

def display_translation():

    global curr_word
   
    canvas.itemconfig(canvas_image, image=back_image)
    language_label.config(text="English", bg=BACK_CARD_COLOR,fg="white")
    
    word_label.config(text=curr_word.iloc[0].at["English"],bg=BACK_CARD_COLOR, fg="white")
    


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy")
window.config( padx=50, pady=50, bg=BACKGROUND_COLOR)

#image canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_image = PhotoImage(file=r".\day31-flash_card\images\card_back.png")
front_image = PhotoImage(file=r".\day31-flash_card\images\card_front.png")
canvas_image = canvas.create_image(400, 526/2, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)



# ---------------------------- Labels ------------------------------- #

language_label = Label(font=LANGUAGE_FONT)
language_label.grid(column=0, row= 0 , columnspan=2, sticky="n", pady=100)

word_label = Label(font=WORD_FONT)
word_label.grid(column=0, row=0, columnspan=2)

flip_timer = window.after(1, func=display_translation)
next_word()



# ---------------------------- buttons ------------------------------- #

my_image_right = PhotoImage(file=r".\day31-flash_card\images\right.png")
right_button = Button(image=my_image_right, highlightthickness=0, bd=0, height=100, width=100, command=next_word)
right_button.grid(column=1, row=1)

my_image_wrong = PhotoImage(file=r".\day31-flash_card\images\wrong.png")
wrong_button = Button(image=my_image_wrong, highlightthickness=0, bd=0, height=100, width=100, command=next_word)
wrong_button.grid(column=0, row=1)




window.mainloop()

