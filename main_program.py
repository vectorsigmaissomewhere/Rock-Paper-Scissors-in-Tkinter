import tkinter as tk
import pygame
import random


pygame.mixer.init()
pygame.mixer.music.load('cara.mp3')
pygame.mixer.music.play(-1)  

def set_volume(val):
    volume = float(val) / 100  
    pygame.mixer.music.set_volume(volume)

def on_closing():
    pygame.mixer.music.stop() 
    window.destroy()

window = tk.Tk()
window.title("ROCK PAPER SCISSORS")
window.geometry("800x550")
window.configure(bg="black")


frameCnt = 12
frames = [tk.PhotoImage(file='caramelldansen-dance.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    window.after(100, update, ind)
label = tk.Label(window)
label.pack()
window.after(0, update, 0)

volume_label = tk.Label(window, text="Volume", bg="black",fg="white",font="Georgia")
volume_label.place(x = 650, y = 20)

volume_scale = tk.Scale(window, from_ = 0, to = 100, orient=tk.HORIZONTAL, command = set_volume,troughcolor = "white",bg = "#ffe100")
volume_scale.set(50) 
volume_scale.place(x = 650, y = 50)

firstplayerframe = tk.Frame(
    window,
    bg = "#3a1cd4",
    height = 150,
    width = 250
)
firstplayerframe.place(x = 100, y = 300)
firstplayerlabel = tk.Label(firstplayerframe,text = "Rock Paper Scissor",width = 15,height = 1,font = ("Arial",12))
firstplayerlabel.place(x = 50,y = 50)

yourframe = tk.Frame(
    window,
    bg = "#3a1cd4",
    height = 150,
    width = 250
)
yourframe.place(x = 500, y = 300)
yourframelabel = tk.Label(yourframe,text = "Rock Paper scissors",width = 15,height = 1,font = ("Arial",12))
yourframelabel.place(x = 50,y = 50)


chosen = ""
def youchoserock():
    global chosen
    chosen = "rock"
    random_choice()
    yourframelabel.config(text = "Rock")
    mainresult()
    

def youchosepaper():
    global chosen
    chosen = "paper"
    random_choice()
    yourframelabel.config(text = "Paper")
    mainresult()
    

def youchosescissors():
    global chosen
    chosen = "scissors"
    random_choice()
    yourframelabel.config(text="Scissors")
    mainresult()



rockbutton = tk.Button(yourframe, text = "Rock", fg = "black", bg = "white", command = youchoserock,font = ("Arial",12))
rockbutton.place(x = 20, y = 90)

paperbutton = tk.Button(yourframe, text = "Paper", fg = "black", bg = "white", command = youchosepaper,font = ("Arial",12))
paperbutton.place(x = 75, y = 90)

scissorsbutton = tk.Button(yourframe, text="Scissors", fg="black", bg = "white", command = youchosescissors,font = ("Arial",12))
scissorsbutton.place(x = 135, y = 90)

result_label = tk.Label(
    window,
    text = "running",
    font = ("Trebuchet Ms", 15, "bold"),
    fg = "white",
    bg = "black"
)
result_label.place(x = 350, y = 450)
  
def random_choice():
    randomchosen = ["rock", "paper", "scissors"]
    run = random.randint(0,2)
    global otherplayerchosen
    otherplayerchosen = randomchosen[run]
    firstplayerlabel.config(text = (otherplayerchosen).capitalize())
def mainresult():
  
  if chosen == "rock":
    if otherplayerchosen == "rock":
      result_label.config(text = "Draw")
    elif otherplayerchosen == "paper":
      result_label.config(text = "Other player won")
    elif otherplayerchosen == "scissors":
      result_label.config(text = "You won")
  elif chosen == "paper":
    if otherplayerchosen == "rock":
      result_label.config(text = "you won")
    elif otherplayerchosen == "paper":
      result_label.config(text = "draw")
    elif otherplayerchosen == "scissors":
      result_label.config(text = "Other player Won")
  elif chosen == "scissors":
    if otherplayerchosen == "rock":
      result_label.config(text = "Other Player won")
    elif otherplayerchosen == "paper":
      result_label.config(text = "You Won")
    elif otherplayerchosen == "scissors":
      result_label.config(text = "Draw")
window.protocol("WM_DELETE_WINDOW", on_closing)
window.resizable(False, False)
window.mainloop()


