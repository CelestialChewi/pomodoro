from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20




# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="#f7f5dd")


title_label = Label(text="Timer", fg=GREEN, bg="#f7f5dd", font=("Courier", 30, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(103, 130, text="00:00", fill="white", font=("Courier", 33, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN, bg="#f7f5dd", font=("Courier", 15))
check_marks.grid(column=1, row=3)


window.mainloop()