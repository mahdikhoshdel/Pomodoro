from tkinter import *
import math

LOGO_PATH = "tomato.png"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Courier", 25, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    main_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_face, text="00:00")
    check_mark_label.config(text="")


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        main_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        main_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        main_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_face, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✅"
        check_mark_label.config(text=marks)


# UI setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Tomato background
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file=LOGO_PATH)
canvas.create_image(100, 112, image=tomato_image)
timer_face = canvas.create_text(100, 130, text="00:00", fill="white", font=FONT)
canvas.grid(column=1, row=1)

# labels
main_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=FONT)
main_label.grid(column=1, row=0)
check_mark_label = Label(bg=YELLOW, fg=GREEN)
check_mark_label.grid(column=1, row=3)

# buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
