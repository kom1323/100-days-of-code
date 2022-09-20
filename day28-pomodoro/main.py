from cgitb import reset
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
reps = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global my_timer, reps
    reps = 0
    window.after_cancel(my_timer)
    my_timer = None
    canvas.itemconfig(timer_text, text="00:00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_mark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps 
    if reps  == 1:
        return
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        title_label.config(text="Work")
    elif reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_seconds = count % 60
    count_minutes = (count // 60) % 60
    count_hours = (count // 60**2) % 24
    canvas.itemconfig(timer_text, text=f"{count_hours:02d}:{count_minutes:02d}:{count_seconds:02d}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        if reps % 2 == 0:
            check_mark_label["text"] += "✔"        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r".\day28-pomodoro\tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check_mark_label.grid(column=1, row=3)





window.mainloop()