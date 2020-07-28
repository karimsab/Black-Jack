# Blackjack

Démonstration de l'utilisation de la librairie `Tkinter`dans l'élaboration d'un code `Python`du jeu de **Blackjack**.

1. Fenêtre Tkinter

On importe le module:
`from tkinter import *`
On crée la fenêtre, le titre ainsi que la taille de la fenêtre:
```
root = Tk()
root.title("Blackjack")
root.geometry("500x640")
```
Ligne de code permettan l'affichage de la fenêtre:
`root.mainloop()`

![Capture d’écran 2020-07-28 à 15 27 27](https://user-images.githubusercontent.com/62601686/88671856-149bd080-d0e7-11ea-8804-a5ecc0532723.png)

2. Création du canevas
Le canevas créé nous servira de support de dessin. Dessus on pourra afficher des images, du texte, ou dessiner des formes prédéfinies.
En même temps, on place nos boutons au bas de la fenêtre qui vont nous permettre d'agir lors du jeu.
