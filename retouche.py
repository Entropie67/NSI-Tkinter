from tkinter import *
from tkinter.messagebox import *
#from PIL.Image import *
import random

"""
image=open("IMAGE.jpg")
(L,H)= image.size
for i in range(H): # On parcours les lignes de pixels de l'image
    for j in range(L): # On parcours les pixels de la ligne i
        image.putpixel((j, i), (0, 0, 255))
image.save("resultat.jpg", "JPEG")
"""

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
    showinfo("Fonction lancée")

    print(variable.get())
    return random.choice(jours)

# On crée la fenêtre principale
fenetre = Tk()
fenetre.title("Mon logiciel")
fenetre['bg']='#FA8072'

frame1 = Frame(fenetre, borderwidth=5, relief=GROOVE)
frame1.pack(side=LEFT,expand = True, fill = BOTH, padx=10, pady=10)
frame2 = Frame(fenetre, borderwidth=5, relief=GROOVE)
frame2.pack(side=LEFT,expand = True, fill = BOTH, padx=10, pady=10)
# On crée un petit label
label = Label(frame1, text="Image de départ")
label.pack()
label = Label(frame2, text="Image modifiée")
label.pack()

bouton_choix = Button(frame1, text="Choix", command=choix)
bouton_choix.pack(side = BOTTOM, padx = 10, pady = 10)

# on crée un bouton
bouton = Button(fenetre, text="Quit", command=fenetre.destroy)
bouton.pack(side=BOTTOM, expand = True, fill = BOTH, padx = 10, pady = 10)

# Un input
variable = StringVar()
variable.set(str(choix()))
entre = Entry(frame2, textvariable=variable, width=50, bg = '#999999', fg='blue')
entre.pack(side = LEFT, padx = 10, pady = 10)

image = PhotoImage(file="image/pomme.png")
canvas = Canvas(frame1, width=400, height=400)
canvas.create_image(0,0, anchor=NW, image=image)
canvas.pack(side=RIGHT)

fenetre.mainloop()

