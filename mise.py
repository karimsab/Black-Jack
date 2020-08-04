from tkinter import *
from time import sleep
from random import randrange

root = Tk()
root.title("Blackjack")
root.geometry("500x640")


# Création du canevas
can = Canvas(root, height=600, width=500, highlightthickness=0, bg ='green')
can.pack(side=TOP, padx=5, pady=5)

b2 = Button(root, text ='Quitter', width=15, command=root.quit)
b2.pack(side=RIGHT)

def miser(event):
    global jeton, total, tot
    objet = can.find_closest(event.x, event.y)
    jeton = objet[0]
    if jeton in [1, 3, 5]:
        deplacement()
    if jeton == 1:
        total += 10
    elif jeton == 3:
        total += 20
    elif jeton == 5:
        total += 50
    can.delete(tot)
    can.create_text(360, 300, text=total, fill='#640809', font='Arial 18 bold')
    can.update()


def deplacement():
    global dx, dy, jeton
    if can.coords(jeton)[1] < 270:
        can.delete(jeton)
        can.delete(jeton+1)
    can.move(jeton, dx, dy)
    can.move(jeton+1, dx, dy)
    root.after(10, deplacement)

 
#Deplacement de la balle au départ:
dx=0
dy=-5

total = 0

jeton10 = can.create_oval(250,450,300,500,fill='#f3df10', width=8, outline='#9b8f09')
dix = can.create_text(274, 475, text='10', fill='white', font='Times 18 bold')
jeton20 = can.create_oval(320,450,370,500,fill='#0a1ab1', width=8, outline='#08105b')
vingt = can.create_text(344, 475, text='20', fill='white', font='Times 18 bold')
jeton50 = can.create_oval(390,450,440,500,fill='#f41005', width=8, outline='#700b07')
cinquante = can.create_text(414, 475, text='50', fill='white', font='Times 18 bold')

stack = can.create_rectangle(240,250,450,350, fill='', width=8, outline='#bcbc0b')
m = can.create_text(320, 300, text='MISE : ', fill='#640809', font='Arial 18 bold')
tot = can.create_text(360, 300, text=total, fill='#640809', font='Arial 18 bold')

root.bind("<Button-1>", miser)

root.mainloop()