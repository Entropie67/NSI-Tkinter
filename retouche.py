from tkinter import *
from tkinter.messagebox import *
from PIL.Image import *
from PIL import Image, ImageTk
import random

chemin = "image/pomme.jpg"
originale = open("image/pomme.jpg")

def negatif():

    (L,H)= originale.size
    nouvelle_image = new("RGB", (L, H))
    for i in range(H): # On parcours les lignes de pixels de l'image
        for j in range(L): # On parcours les pixels de la ligne i
            (r, v, b) = originale.getpixel((j, i))
            nouvelle_image.putpixel((j, i), (255 - r, 255 - v, 255 - b))
    nouvelle_image.save("image/resultat.jpg", "JPEG")
    variable.set("image/resultat.jpg")
    canvas2.itemconfig(1, image=image2)


# On crée la fenêtre principale avec un titre et un fond
fenetre = Tk()
fenetre.title("PhotoSturm")
fenetre['bg'] = '#FA8072'


# On crée un petit label
# On crée les titres des deux parties principale de l'appli
titre_depart = Label(fenetre, text="Image de départ")
titre_fin = Label(fenetre, text="Image modifiée")

titre_depart.grid(row = 0, column = 0, sticky = N, pady = 2)
titre_fin.grid(row = 0, column = 2, sticky = N, pady = 2)

bouton_choix = Button(fenetre, text="Négatif", command=negatif)
bouton_choix.grid(row = 2, column = 0, sticky = W, pady = 2)

# Un input
variable = StringVar()
variable.set(chemin)
entre = Entry(fenetre, textvariable=variable, width=50, bg = '#999999', fg='blue')
entre.grid(row = 2, column = 2, sticky = W, pady = 2)

image = ImageTk.PhotoImage(originale)
canvas = Canvas(fenetre, width=400, height=400)
canvas.create_image(50, 5, anchor=NW, image=image)
canvas.grid(row = 1, column = 0, sticky = W, pady = 2)

image2 = ImageTk.PhotoImage(Image.open("image/resultat.jpg"))

canvas2 = Canvas(fenetre, width=400, height=400)
i =canvas2.create_image(0, 0, anchor=NW, image=image)
print(i)

canvas2.grid(row = 1, column = 2, sticky = W, pady = 2)


# Le bouton qui permet de quitter l'application.
bouton = Button(fenetre, text="Quit", fg="red", bg="white", relief="raised", overrelief ="sunken", command=fenetre.destroy)
bouton.grid(row = 3, column = 1, sticky = W, pady = 2)

fenetre.mainloop()

