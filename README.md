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

2. Création du canevas

Le canevas créé nous servira de support de dessin. Dessus on pourra afficher des images, du texte, ou dessiner des formes prédéfinies.
En même temps, on place nos boutons au bas de la fenêtre qui vont nous permettre d'agir lors du jeu.

```
can = Canvas(root, height=600, width=500, highlightthickness=0, bg ='green')
can.pack(side=TOP, padx=5, pady=5)

b2 = Button(root, text ='Quitter', width=15, command=root.quit)
b2.pack(side=RIGHT)
b1 = Button(root, text ='Carte !', width=15, command=hit)
b1.pack(side=LEFT)
b1 = Button(root, text ='Je reste', width=15, command=stay)
b1.pack(side=LEFT)
```

![Capture d’écran 2020-07-28 à 15 30 51](https://user-images.githubusercontent.com/62601686/88672110-604e7a00-d0e7-11ea-8b45-6b49fb3ae40a.png)

3. Création de classes

`Python`étant un langage de programmation orienté objet, on va donc pouvoir utiliser des classes afin de profiter de la notion d'**héritage** entre objet et ainsi pouvoir utiliser des 'objets' qui ont les mêmes caractéristiques que d'autres 'objets'. En l'occurence, ici, les objets qui vont hériter des caractéristiques, découlent d'objets **parents** (le code suivant n'est posté qu'à titre informatif, il ne produit rien) :

```
class Carte(object):
    def __init___(self):
        pass
        
class Paquet(Carte):
    def __init__(self):
        super().__init__(self)

class Joueur(object):
    def __init__(self):
        pass
```

4. Affichage des cartes

On utilisera 52 cartes sous format .png, qu'on affichera dans le canevas, aux coordonnées souhaitées, ici x = 100, y = 450. L'origine du repère se trouvant en haut à gauche de la fenêtre.
```
can.create_image(100, 450, image=carte)
can.update()
``` 
![Capture d’écran 2020-07-28 à 15 44 54](https://user-images.githubusercontent.com/62601686/88673784-5168c700-d0e9-11ea-8b0d-f4868e1697e4.png)

5. Déroulement du jeu

Pour ceux qui n'auraient jamais joué au Blackjack, le but étant d'avoir une somme de points supérieure à l'adversaire (en général le casino). Si, à l'issue de la distribution initiale des cartes, la somme de nos points vaut 21 points, il y a *Blackjack* et on remporte la mise. Sinon, on demande des cartes pour se rapprocher de 21, si on dépasse 21, on perd la mise.

---

L'idée d'écriture de ce code m'est venu au cours de mes pérégrinations virtuelles, à la recherche de projets en Python. J'ai donc découvert le site d'un professeur de mathématiques, qui permet d'apprendre à la programmation python, en codant divers jeux :

[objectif jeux](http://www.apprendre-en-ligne.net/pj/index.html)

Site très ludique et pédagogique qu permet de s'exercer sur la programmation, dans une difficulté montante.

Ainsi, l'écriture du code est inspirée de ce qu'on peut voir sur le site du professeur.

---

Le résultat final donne ceci :


![Capture d’écran 2020-07-28 à 16 22 45](https://user-images.githubusercontent.com/62601686/88678291-96dbc300-d0ee-11ea-9534-e42e974489b9.png)

De nombreuses améliorations sont possibles, telles que l'ajout de mises et d'images de jeton. L'ajout de joueurs supplémentaires, etc. Afin de rendre le jeux plus prenant.
