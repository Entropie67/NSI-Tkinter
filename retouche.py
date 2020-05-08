from tkinter import *
import random



def choix():
    jours = [
        "lundi",
        "mardi",
        "mercredi",
        "jeudi",
        "vendredi",
        "samedi",
        "dimanche"
    ]
    print(random.choice(jours))
    return random.choice(jours)

# On crée la fenêtre principale
fenetre = Tk()

# On crée un petit label
label = Label(fenetre, text="Choix d'un jour !")
label.pack()

bouton_choix = Button(fenetre, text="Choix", command=choix)
bouton_choix.pack()

# on crée un bouton
bouton = Button(fenetre, text="Quit", command=fenetre.destroy)
bouton.pack()

# Un input
variable = StringVar()
variable.set("Tapez votre texte")
entre = Entry(fenetre, textvariable=variable, width=50)
entre.pack()



fenetre.mainloop()

