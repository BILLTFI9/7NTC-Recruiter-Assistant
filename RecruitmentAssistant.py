from datetime import datetime, timedelta
from tkinter import Frame, ttk
import tkinter as tk
import pygame
import os
import sys

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path) # type: ignore
    return os.path.join(os.path.abspath("."), relative_path)

ntc_logo = r"""                                                
  ______ _   _ _______ _____ 
 |____  | \ | |__   __/ ____|
     / /|  \| |  | | | |     
    / / | . ` |  | | | |     
   / /  | |\  |  | | | |____ 
  /_/   |_| \_|  |_|  \_____|
  
"""
print(ntc_logo)

global countdown_after_id 
countdown_after_id = None
global countdown_cycle_count
countdown_cycle_count = 0

pygame.mixer.init()
pygame.mixer.music.load(get_resource_path('WindChimes.wav'))

def calculate_time(): # Screenshot time calculator
    start_time = time_var.get()
    output_text.delete('1.0', tk.END)

    global countdown_after_id 
    countdown_after_id = None
    global countdown_cycle_count
    countdown_cycle_count = 0

    try:
        dtime_timevar = datetime.strptime(start_time, "%H:%M")

        for x in range(1, 10):
            output_text.insert(tk.END, f"Pic {x}: {dtime_timevar.strftime('%H:%M')}\n")
            print(f"Pic {x}: {dtime_timevar.strftime('%H:%M')}")
            dtime_timevar += timedelta(minutes=15)
        print("----------------")

        countdown_label.config(text="Starting countdown")
        start_timer(899)

    except ValueError:
        output_text.insert(tk.END, "Learn to type :[")
        print("Learn to type :[\n----------------")
        countdown_label.config(text="Error")

    output_text.tag_add("center", "1.0", "end")

def start_timer(seconds_left):
    global countdown_after_id
    if countdown_after_id:
        window.after_cancel(countdown_after_id)
    
    update_countdown(seconds_left)

def update_countdown(temp_seconds):
    global countdown_after_id
    global countdown_cycle_count

    if temp_seconds > 0:
        mins, secs = divmod(temp_seconds, 60)
        time_str = " {:02d}:{:02d}".format(mins, secs)
        countdown_label.config(text=time_str)
        print(time_str, end="\r")

        countdown_after_id = window.after(1000, update_countdown, temp_seconds - 1)
    else:
        countdown_cycle_count += 1

        if countdown_cycle_count < 8:
            print(f"\nCycle {countdown_cycle_count} Done!")
            pygame.mixer.music.play(loops=0)
            start_timer(899)

        else:
            pygame.mixer.music.play(loops=0)
            countdown_label.config(fg="#C70000")
            countdown_label.config(text="Touch grass")
            print("\nTouch grass")
            countdown_after_id = None


#-------------- Window & Tabs --------------
window = tk.Tk()
window.iconbitmap(get_resource_path("RecruiterAssistantV1.3.ico"))
notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab1.config(bg="#393E46")
tab2 = Frame(notebook)
tab2.config(bg="#393E46")

# Tabs
notebook.add(tab1, text="Screenshot Timer")
notebook.add(tab2, text="Notepad")

notebook.pack(expand=True, fill="both")

window.geometry("400x550") # Window Size
window.minsize(400, 550)
window.config(bg="#393E46")
window.title("7NTC Recruiter Assistant v1.3") # Window Title

#-------------- Screenshot Timer --------------
logo = tk.Label(tab1, text="Screenshot Timer", font=('Arial', 18))
logo.pack(padx=10, pady=30)

time_var = tk.StringVar()

time_label = tk.Label(tab1, text='Enter initial screenshot time (ex. 08:14):', font=('Arial', 16))
time_label.pack(padx=10, pady=2)

time_entry = tk.Entry(tab1, textvariable=time_var, font=('Arial', 16))
time_entry.config(bg="#C7C7C7")
time_entry.pack(padx=10, pady=5)
time_entry.focus()

submit = tk.Button(tab1, text="Calculate Screenshot times", command=calculate_time , font=('Arial', 16))
submit.pack(padx=10, pady=5)

countdown_label = tk.Label(tab1, text="Hello :]", font=('Arial', 16, 'bold'), height=1, width= 10, fg="#FFD700", bg="#393E46")
countdown_label.pack(padx=10, pady=10)

output_text = tk.Text(tab1, height=9 , width=12, font=('Arial', 16))
output_text.tag_configure("center", justify='center')
output_text.config(bg="#C7C7C7")
output_text.pack(padx=30, pady=20)

my_name = tk.Label(tab1, text="Billtfi (BILLTFI9)", font=('Arial', 10), fg="#C7C7C7", bg="#393E46")
my_name.place(relx=1.0, rely=1.0, anchor='se', x=-5, y=-5)

#-------------- Notepad --------------
logo = tk.Label(tab2, text="Notepad", font=('Arial', 18))
logo.pack(padx=10, pady=30)

notepad = tk.Text(tab2, height=15, width=28, font=('Arial', 16))
notepad.pack(padx=25, pady=25)

my_name = tk.Label(tab2, text="Billtfi (BILLTFI9)", font=('Arial', 10), fg="#C7C7C7", bg="#393E46")
my_name.place(relx=1.0, rely=1.0, anchor='se', x=-5, y=-5)

window.mainloop() # End of Window
