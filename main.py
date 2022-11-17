from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    if reps % 2 == 0:
        count_down(WORK_MIN * 60)
        title_label.config(text="WORK", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
    elif reps % 8 == 7:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="BREAK", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=RED)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="BREAK", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    mm = int(count / 60)
    ss = count % 60
    canvas.itemconfig(timer_text, text=f"{mm:02d}:{ss:02d}")
    if count > 0:
        global timer
        timer = window.after(100, count_down, count - 1)
    else:
        marks = ""
        for _ in range(int(reps / 2)):
            marks += "✓"
            checks.config(text=marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

checks = Label(font=(FONT_NAME, 18, "bold"), bg=YELLOW, fg=GREEN)
checks.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
