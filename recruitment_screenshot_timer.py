from datetime import datetime, timedelta
from tkinter import Frame, ttk
import tkinter as tk

ntc_logo = r"""                                                
  ______ _   _ _______ _____ 
 |____  | \ | |__   __/ ____|
     / /|  \| |  | | | |     
    / / | . ` |  | | | |     
   / /  | |\  |  | | | |____ 
  /_/   |_| \_|  |_|  \_____|
  
"""
print(ntc_logo)

def calculate_time():
    start_time = time_var.get()
    output_text.delete('1.0', tk.END)
    try:
        dtime_timevar = datetime.strptime(start_time, "%H:%M")

        for x in range(1, 10):
            output_text.insert(tk.END, f"Pic {x}: {dtime_timevar.strftime('%H:%M')}\n")
            print(f"Pic {x}: {dtime_timevar.strftime('%H:%M')}")
            dtime_timevar += timedelta(minutes=15)
        print("----------------")

    except ValueError:
        output_text.insert(tk.END, "Learn to type :[")
        print("Learn to type :[\n----------------")

    output_text.tag_add("center", "1.0", "end")


window = tk.Tk()
notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab1.config(bg="#393E46")
tab2 = Frame(notebook)
tab2.config(bg="#393E46")

notebook.add(tab1, text="Screenshot Timer")
notebook.add(tab2, text="Notes")

notebook.pack(expand=True, fill="both")

window.geometry("800x500")
window.config(bg="#393E46")
window.title("7NTC Recruiter Assistant v1.0")
logo = tk.Label(tab1, text="7NTC Recruiter Assistant v1.0", font=('Arial', 18))
logo.pack(padx=10, pady=30)

time_var = tk.StringVar()

time_label = tk.Label(tab1, text='Enter initial screenshot time (ex. 08:14):', font=('Arial', 16))
time_label.pack(pady=2)

time_entry = tk.Entry(tab1, textvariable=time_var, font=('Arial', 16))
time_entry.config(bg="#C7C7C7")
time_entry.pack(pady=5)
time_entry.focus()

submit = tk.Button(tab1, text="Calculate Screenshot times", command=calculate_time , font=('Arial', 16))
submit.pack(pady=5)

output_text = tk.Text(tab1, height=9 , font=('Arial', 16))
output_text.tag_configure("center", justify='center')
output_text.config(bg="#C7C7C7")
output_text.pack(padx=325, pady=30)

my_name = tk.Label(tab1, text="Billtfi (BILLTFI9)", font=('Arial', 10), fg="#C7C7C7", bg="#393E46")
my_name.place(relx=1.0, rely=1.0, anchor='se', x=-5, y=-5)

window.mainloop()
