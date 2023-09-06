import tkinter as tk
from tkinter import ttk
import subprocess

window = tk.Tk()
window.title("Hello World")

# Load the background image and resize it
image = tk.PhotoImage(file="opening.png")
width = image.width() // 2  
height = image.height() // 2  
image = image.subsample(2, 2)  

bg_label = tk.Label(window, image=image)
bg_label.place(x=0, y=0)


screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2
window.geometry(f"{width}x{height}+{x}+{y}")


welcome_label = tk.Label(
    text="Your Application Name",
    bg="#26C680",
    font=("Trebuchet Ms", 15, "bold"),
    fg="#FFFFFF",
)
welcome_label.place(x=130, y=25)


progress_label = tk.Label(
    window,
    text="Loading...",
    font=("Trebuchet Ms", 13, "bold"),
    fg="#FFFFFF",
    bg="#2F6C60",
)
progress_label.place(x=450, y=400)

progress = ttk.Progressbar(
    window,
    orient=tk.HORIZONTAL,
    length=400,
    mode="determinate",
    style="red.Horizontal.TProgressbar",
)
progress.place(x=330, y=450)


def top():
    window.withdraw()
    subprocess.run(["python", "main_program.py"])
    window.destroy()

i = 0


def load():
    global i
    if i <= 10:
        txt = 'Loading... ' + str(10 * i) + '%'
        progress_label.config(text=txt)
        progress_label.after(600, load)
        progress['value'] = 10 * i
        i += 1
    else:
        top()

load()
window.resizable(False, False)
window.mainloop()
