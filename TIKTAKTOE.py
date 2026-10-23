#IMPORTS
import tkinter as tk
import random
import time
first=0
mx=0
my=0
info= [0,0,0,0,0,0,0,0,0]
player= random.randint(1, 2)

#SETUP_WINDOW
window = tk.Tk()
window.title("BLEH")
window.geometry("325x300")
canvas = tk.Canvas(window, width=(325), height=(300), bg="white")
canvas.pack()
label = tk.Label(window, text="x: 0 y: 0")
label.pack()

#mouse pos
def mouse_pos(event):
    global mx, my
    mx, my = event.x, event.y
canvas.bind("<Motion>", mouse_pos)


#click detect
def mouse_click(event):
    global mx, my,info,player
    if round(mx/100-0.5)<= 2 and info[(round(mx/100-0.5)+round(my/100-0.5)*3)]==0:
        info[(round(mx/100-0.5)+round(my/100-0.5)*3)]=player
        render()
        win()
        if player ==1:
            player=2
        else:
            player=1

canvas.bind("<Button-1>", mouse_click)





#RENDER SCREEN
def render():
    global first
    weg=0
    y=0
    canvas.delete("all")
    for i in range(3):
        x=0
        for i in range(3):
            if info[weg]==0:
                cube = canvas.create_rectangle(x, y, x + 100, y + 100, fill="white")
            elif info[weg]==1:
                cube = canvas.create_rectangle(x, y, x + 100, y + 100, fill="white")
                line = canvas.create_line(x+10, y+10, x+90, y+90, fill="red", width=4)
                line = canvas.create_line(x+90, y+10, x+10, y+90, fill="red", width=4)
            elif info[weg]==2:
                cube = canvas.create_rectangle(x, y, x + 100, y + 100, fill="white")
                canvas.create_oval(x+10, y+10, x+90, y+90, outline='blue', fill='white', width=4)
            x+=100
            weg+=1
        y+=100
    if first==0:
        if player ==1:
            cube = canvas.create_rectangle(300,0,325,300, fill="red")
        else:
            cube = canvas.create_rectangle(300,0,325,300, fill="blue")
        first=1
    else:
        if player ==2:
            cube = canvas.create_rectangle(300,0,325,300, fill="red")
        else:
            cube = canvas.create_rectangle(300,0,325,300, fill="blue")


#WIN DETECT >:3
def win():
    if info[0]==player and info[1]==player and info[2]==player:
        won()
    elif info[3]==player and info[4]==player and info[5]==player:
        won()
    elif info[6]==player and info[7]==player and info[8]==player:
        won()
    elif info[0]==player and info[3]==player and info[6]==player:
        won()
    elif info[1]==player and info[4]==player and info[7]==player:
        won()
    elif info[2]==player and info[5]==player and info[8]==player:
        won()
    elif info[0]==player and info[4]==player and info[8]==player:
        won()
    elif info[2]==player and info[4]==player and info[6]==player:
        won()
    elif all(info):
        won(True)

#RESET AND WON :O
def won(tie=False):
    global player,info
    canvas.delete("all")
    if tie:
        cube = canvas.create_rectangle(0,0,325,300, fill="grey")
        canvas.create_text(162, 150, text=("A TIE"), fill="black", font=("Arial", 20))
    else:
        if player ==1:
            cube = canvas.create_rectangle(0,0,325,300, fill="red")
        elif player==2:
            cube = canvas.create_rectangle(0,0,325,300, fill="blue")
        canvas.create_text(162, 150, text=("PLAYER",str(player),"WON"), fill="black", font=("Arial", 20))
    info= [0,0,0,0,0,0,0,0,0]
    player=random.randint(1, 2)
    window.after(3000, render)



#WINDOW LOOPS
render()
window.mainloop()
