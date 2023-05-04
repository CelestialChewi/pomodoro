from tkinter import *
import math

# Variables where you can change

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# Reset Timer Mechanism-------------------------------
reps = 0
timer = None

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# Start Timer Mechanism-------------------------------
def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0: # 8th reps
        countdown(long_break_seconds)
        title_label.config(text="Break", fg="#e7305b")
    elif reps % 2 == 0: # 2nd, 4th and 6th reps
        countdown(short_break_seconds)
        title_label.config(text="Break", fg="#e2979c")
    else: # 1st, 3rd, 5th and 7th reps
        countdown(work_seconds)
        title_label.config(text="Work", fg="#9bdeac")


# Countdown Mechanism-------------------------------
def countdown(count):
    countdown_minutes = math.floor(count / 60)
    countdown_seconds = count % 60
    if countdown_seconds < 10:
        countdown_seconds = f"0{countdown_seconds}"

    if countdown_minutes < 10:
        countdown_minutes = f"0{countdown_minutes}"
    canvas.itemconfig(timer_text, text=f"{countdown_minutes}:{countdown_seconds}")
    
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for session in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)


# UI Setup-------------------------------
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="#f7f5dd")


title_label = Label(text="Timer", fg="#9bdeac", bg="#f7f5dd", font=("Courier", 30, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=("Courier", 33, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2, command=reset_timer)

check_marks = Label(fg="#9bdeac", bg="#f7f5dd", font=("Courier", 15))
check_marks.grid(column=1, row=3)


window.mainloop()