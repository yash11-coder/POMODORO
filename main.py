from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="TIMER", fg=GREEN)
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+= 1
    work_sec = int(WORK_MIN*60)
    short_break_sec = int(SHORT_BREAK_MIN*60)
    long_break_sec = int(LONG_BREAK_MIN*60)

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)

    elif reps%2 ==0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count/60)
    if count_min <= 9:
        count_min = f"{0}{count_min}"
    count_sec = count%60
    if count_sec <= 9:
        count_sec = f"{0}{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = int(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
tomoto_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomoto_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)



timer_label = Label(text="TIMER", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)


start_button = Button(text="Start", font=(FONT_NAME,10, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME,10, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


check_marks = Label(font=(FONT_NAME,15, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)





window.mainloop()