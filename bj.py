from tkinter import *
from time import sleep
from random import randrange

root = Tk()
root.title("Blackjack")
root.geometry("500x640")

point = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
valeur = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi']
couleur = ['pique', 'trefle', 'coeur', 'carreau']

class Carte(object):
    def __init__(self, val, coul, point):
        self.valeur = val
        self.couleur = coul
        self.point = point
    
    def affiche(self):
        nom = "cartes/" + self.valeur + "_" + self.couleur + ".gif"
        return PhotoImage(file=nom)

class Paquet(object):
    def __init__(self):
        self.cartes = []
        for coul in range(4):
            for val in range(13):
                carte = Carte(valeur[val], couleur[coul], point[val])
                self.cartes.append(carte)
    
    def melanger(self):
        for i in range(len(self.cartes)):
            c1, c2 = randrange(len(self.cartes)), randrange(len(self.cartes))
            self.cartes[c1], self.cartes[c2] = self.cartes[c2], self.cartes[c1]
        return self.cartes
    
    def tirer(self):
        n = len(self.cartes)
        if n > 0:
            return self.cartes.pop()
        else:
            return None

class Joueur(object):
    def __init__(self):
        self.main = []
    
    def ajouter(self, c):
        return self.main.append(c.point)
    
    def points(self):
        return calculer(self.main)

    def reinit(self):
        self.main = []

def calculer(cartes):
    pts = 0
    nb_as = cartes.count(1)
    for c in cartes:
        if c > 1:
            pts += c
    if nb_as == 0:
        return pts
    else:
        if nb_as == 4 and pts <= 7:
            return pts + 14
        elif nb_as == 4 and pts > 7:
            return pts + 4
        if nb_as == 3 and pts <= 8:
            return pts + 13
        elif nb_as == 3 and pts > 8:
            return pts + 3
        if nb_as == 2 and pts <= 9:
            return pts + 12
        elif nb_as == 2 and pts > 9:
            return pts + 2
        if nb_as == 1 and pts <= 10:
            return pts + 11
        elif nb_as == 1 and pts > 10:
            return pts + 1

def reinit():
    global jeu, can, mes_cartes, ses_cartes, moi, banque, mon_total, son_total, mes_points, ses_points
    moi.reinit()
    banque.reinit()
    mes_cartes = []
    ses_cartes = []
    jeu.melanger()
    can.delete(ALL)
    can.create_text(60, 30, text='Banque : ')
    can.create_text(60, 340, text='Joueur : ')

    c1 = jeu.tirer()
    mes_cartes.append(c1.affiche())
    moi.ajouter(c1)
    can.create_image(100, 450, image=mes_cartes[0])
    can.update()
    sleep(1)

    d1 = jeu.tirer()
    ses_cartes.append(d1.affiche())
    banque.ajouter(d1)
    son_total = banque.points()
    can.create_image(100, 150, image=ses_cartes[0])
    ses_points = can.create_text(100, 30, text=son_total)
    can.update()
    sleep(1)

    c2 = jeu.tirer()
    mes_cartes.append(c2.affiche())
    moi.ajouter(c2)
    can.create_image(100+50, 450, image=mes_cartes[1])
    can.update()
    sleep(1)
    mon_total = moi.points()
    if mon_total == 21:
        can.create_text(200, 340, text='Blackjack !', fill='red', font='Arial 18')
        can.update()
        # sleep(6)
        # reinit()

    mes_points = can.create_text(100, 340, text=mon_total)
    can.update()


def hit():
    global jeu, moi, banque, mes_cartes, mes_points, mon_total
    c = jeu.tirer()
    moi.ajouter(c)
    mes_cartes.append(c.affiche())
    mon_total = moi.points()
    n = len(moi.main)
    can.delete(mes_points)
    can.create_image(100+50*(n-1), 450, image=mes_cartes[n-1])
    can.create_text(120, 340, text=mon_total)
    can.update()
    if mon_total > 21:
        can.delete(mes_points)
        can.update()
        can.create_text(200, 340, text='Perdu !', fill='red', font='Arial 18')
        can.update()
        sleep(3)
        reinit()


def stay():
    global jeu, ses_cartes, banque, mon_total, son_total, mes_points, ses_points
    c = jeu.tirer()
    banque.ajouter(c)
    ses_cartes.append(c.affiche())
    son_total = banque.points()
    n = len(banque.main)
    can.delete(ses_points)
    can.create_text(120, 30, text=son_total)
    can.create_image(100+50*(n-1), 150, image=ses_cartes[n-1])
    can.update()

    if son_total > 21:
        can.create_text(200, 340, text='Gagné', fill='red', font='Arial 18')
        can.update()
        # sleep(3)
        # reinit()
    if son_total == 21 and n == 2:
        can.create_text(200, 30, text='Blackjack !', fill='red', font='Arial 18')
        can.update()
        # sleep(6)
        # reinit()
    if son_total >= 17:
        if son_total == mon_total:
            can.create_text(200, 30, text='égalité !', fill='red', font='Arial 18')
            can.create_text(200, 340, text='égalité !', fill='red', font='Arial 18')
            can.update()
        elif son_total > mon_total:
            can.create_text(200, 340, text='Perdu !', fill='red', font='Arial 18')
            can.update()
        elif son_total < mon_total:
            can.create_text(200, 340, text='Gagné !', fill='red', font='Arial 18')
            can.update()
        # sleep(3)
        # reinit()
    elif son_total < 17:
        sleep(2)
        stay()





jeu = Paquet()
moi = Joueur()
banque = Joueur()

mes_cartes = []
ses_cartes = []

# Création du canevas
can = Canvas(root, height=600, width=500, highlightthickness=0, bg ='green')
can.pack(side=TOP, padx=5, pady=5)

b2 = Button(root, text ='Quitter', width=15, command=root.quit)
b2.pack(side=RIGHT)
b1 = Button(root, text ='Carte !', width=15, command=hit)
b1.pack(side=LEFT)
b1 = Button(root, text ='Je reste', width=15, command=stay)
b1.pack(side=LEFT)

reinit()

root.mainloop()