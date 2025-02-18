from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Century Gothic"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = ""
primary_timer = None
paused_min = 0
paused_sec = 0
paused_reps = 0
paused = False

# ---------------------------- TIMER START FROM PAUSE ------------------------------- #

# ---------------------------- TIMER PAUSE / START ------------------------------- #
def pause():
    global paused
    paused = True
    window.after_cancel(primary_timer)


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(primary_timer)
    timer_laber["text"] = "Pomodoro Timer"
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global paused
    if not paused:
        global reps
        reps +=1
        global paused_reps
        paused_reps = reps
        global checkmark
        if reps %8 == 0:
            timer_laber.config(text="Long break")
            countdown(20 * 60)
        elif reps %2 == 0:
            checkmark += "✔"
            checkmark_label.config(text=checkmark)
            timer_laber.config(text="Short break")
            countdown(5 * 60)
        else:
            timer_laber.config(text="Time to work!")
            countdown(25 * 60)
    elif paused:
        paused = False
        countdown(paused_min * 60 + paused_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global primary_timer
    global paused_min
    global paused_sec
    count_min = math.floor(count/60)
    paused_min = count_min
    count_sec = count % 60
    paused_sec = count_sec

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min} : {count_sec}")

    if count > 0:
        primary_timer = window.after(1000, countdown, count-1)
    else:
        start_timer()




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(pady=50,padx=100,bg=YELLOW)
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_photo)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(column=2,row=2)

timer_laber = Label(text="Pomodoro Timer",fg= RED,font=("Courier",30),bg=YELLOW)
timer_laber.grid(column=2,row=1)

checkmark_label = Label(text="",fg= GREEN,font=("Courier",20),bg=YELLOW)
checkmark_label.grid(column=2,row=3)


button = Button(text="Start",font=("Courier",11), command=start_timer)
button.grid(column=1,row=3)

button = Button(text="Pause", font=("Courier",11),command=pause)
button.grid(column=2,row=4)

button = Button(text="Reset", font=("Courier",11),command=reset)
button.grid(column=3,row=3)



window.mainloop()


