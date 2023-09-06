import tkinter as tk
import pygame
import random

# Initialize pygame mixer and load a music file (for demo purposes, I'll use the same 'cara.mp3')
pygame.mixer.init()
pygame.mixer.music.load('cara.mp3')
pygame.mixer.music.play(-1)  # Play the music in a loop

def set_volume(val):
    volume = float(val) / 100  # Scale's values are strings; convert to float and normalize
    pygame.mixer.music.set_volume(volume)

def on_closing():
    pygame.mixer.music.stop()
    window.destroy()

window = tk.Tk()
window.geometry("800x550")
window.configure(bg="#FFFFFF")

welcome_label = tk.Label(window, text="Home")
welcome_label.place(x=133, y=25)

volume_label = tk.Label(window, text="Volume", bg="#FFFFFF")
volume_label.place(x=20, y=20)

volume_scale = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=set_volume)
volume_scale.set(50)  # Default volume level: 50%
volume_scale.place(x=20, y=50)

firstplayerframe = tk.Frame(
    window,
    bg="#C522D4",
    height=150,
    width=200
)
firstplayerframe.place(x=300, y=50)

yourframe = tk.Frame(
    window,
    bg="#C522D4",
    height=150,
    width=200
)
yourframe.place(x=500, y=300)

rockbutton = tk.Button(yourframe, text="Rock", fg="black", bg="white", command="youchoserock")
rockbutton.place(x=20, y=90)

paperbutton = tk.Button(yourframe, text="Paper", fg="black", bg="white", command="youchosepaper")
paperbutton.place(x=75, y=90)

scissorsbutton = tk.Button(yourframe, text="Scissors", fg="black", bg="white", command="youchosescissors")
scissorsbutton.place(x=135, y=90)

chosen = ""
result_label = tk.Label(
    window,
    text="",
    font=("Trebuchet Ms", 15, "bold"),
    fg="#000000",
    bg="#FFFFFF",
)
result_label.place(x=350, y=450)

def youchoserock():
    global chosen
    chosen = "rock"

def youchosepaper():
    global chosen
    chosen = "paper"

def youchosescissors():
    global chosen
    chosen = "scissors"

reverseBackbtn=tk.Button(yourframe,text="Play Again",fg="black",bg="white")
reverseBackbtn.place(x=195,y=90)
def reverseBack():
  global chosen
  chosen=""
  
def random_choice():
    randomchosen = ["rock", "paper", "scissors"]
    run=random.randint(0,2)
    global otherplayerchosen
    otherplayerchosen=randomchosen[run]
def mainresult():
  if chosen.equals("rock"):
    if otherplayerchosen.equals("rock"):
      print("draw")
    elif otherplayerchosen.equals("paper"):
      print("Other player Won")
    elif otherplayerchosen.equals("scissors"):
      print("You won")
  elif chosen.equals("paper"):
    if otherplayerchosen.equals("rock"):
      print("you won")
    elif otherplayerchosen.equals("paper"):
      print("draw")
    elif otherplayerchosen.equals("scissors"):
      print("Other player Won")
  elif chosen.equals("scissors"):
    if otherplayerchosen.equals("rock"):
      print("Other Player won")
    elif otherplayerchosen.equals("paper"):
      print("You Won")
    elif otherplayerchosen.equals("scissors"):
      print("Draw")
      
mainresult()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.resizable(False, False)
window.mainloop()
