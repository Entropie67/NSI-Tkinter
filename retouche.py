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
fenetre.title("Mon logiciel")
fenetre['bg']='#FA8072'

frame1 = Frame(fenetre, borderwidth=5, relief=GROOVE)
frame1.pack(side=LEFT, padx=10, pady=10)
frame2 = Frame(fenetre, borderwidth=5, relief=GROOVE)
frame2.pack(side=LEFT, padx=10, pady=10)
# On crée un petit label
label = Label(frame1, text="Image de départ")
label.pack()
label = Label(frame2, text="Image modifiée")
label.pack()

bouton_choix = Button(frame1, text="Choix", command=choix)
bouton_choix.pack(side = LEFT, padx = 10, pady = 10)

# on crée un bouton
bouton = Button(frame1, text="Quit", command=fenetre.destroy)
bouton.pack(side = LEFT, padx = 10, pady = 10)

# Un input
variable = StringVar()
variable.set(str(choix()))
entre = Entry(fenetre, textvariable=variable, width=50)
entre.pack(side = LEFT, padx = 10, pady = 10)



fenetre.mainloop()

