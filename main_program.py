import tkinter as tk

window = tk.Tk()
window.geometry("800x550")
window.configure(bg="#FFFFFF")
welcome_label = tk.Label(window, text="Home")
welcome_label.place(x=133, y=25)
window.mainloop()
