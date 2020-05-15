from tkinter import *
from tkinter.messagebox import *
from PIL.Image import *
from PIL import Image, ImageTk
import random

chemin = "image/pomme.jpg"
originale = open(chemin)

(L, H) = originale.size
nouvelle_image = new("RGB", (L, H))


def negatif():
    for i in range(H): # On parcours les lignes de pixels de l'image
        for j in range(L): # On parcours les pixels de la ligne i
            (r, v, b) = originale.getpixel((j, i))
            nouvelle_image.putpixel((j, i), (255 - r, 255 - v, 255 - b))
    nouvelle_image.save("image/resultat.jpg", "JPEG")
    variable.set("image/resultat.jpg")
    canvas2.itemconfig(1, image=image2)

def claire():
    for i in range(H):  # On parcours les lignes de pixels de l'image
        for j in range(L):  # On parcours les pixels de la ligne i
            (r, v, b) = originale.getpixel((j, i))
            nouvelle_image.putpixel((j, i), (r + 50, v + 50, b + 50))
    nouvelle_image.save("image/resultat.jpg", "JPEG")
    variable.set("image/resultat.jpg")
    image3 = ImageTk.PhotoImage(nouvelle_image)
    canvas2.itemconfig(1, image=image3)

# On crée la fenêtre principale avec un titre et un fond
fenetre = Tk()
fenetre.title("PhotoSturm")
fenetre['bg'] = '#FA8072'
image_originale = ImageTk.PhotoImage(originale)


# On crée un petit label
# On crée les titres des deux parties principale de l'appli
titre_depart = Label(fenetre, text="Image de départ", padx=10)
titre_fin = Label(fenetre, text="Image modifiée", padx=10)
titre_depart.grid(row=0, column=0, columnspan=6, sticky=N, pady=2, padx=5)
titre_fin.grid(row=0, column=6, columnspan=6, sticky=N, pady=2, padx=5)
bouton_negatif = Button(fenetre, text="Négatif", command=negatif)
bouton_negatif.grid(row=2, column=0, sticky=N, pady=2)
bouton_clair = Button(fenetre, text="Plus clair", command=claire)
bouton_clair.grid(row=2, column=1, sticky=N, pady=2)
bouton_sombre = Button(fenetre, text="Plus sombre", command=claire)
bouton_sombre.grid(row=2, column=2, sticky=N, pady=2)
bouton_save = Button(fenetre, text="Enregistrer", command=negatif, bg = 'green')
bouton_save.grid(row=2, column=8, sticky=N, pady=2)
# Un input
variable = StringVar()
variable.set(chemin)
entre = Entry(fenetre, textvariable=variable, width=50, bg = '#999999', fg='blue')
entre.grid(row=2, column=6, sticky=W, pady=2)




canvas = Canvas(fenetre, width=400, height=400)
canvas.create_image(50, 5, anchor=NW, image=image_originale)
canvas.grid(row=1, column=0, columnspan=6, sticky=N, pady=2)

image2 = ImageTk.PhotoImage(Image.open("image/resultat.jpg"))

canvas2 = Canvas(fenetre, width=400, height=400)
i = canvas2.create_image(0, 0, anchor=NW, image=image_originale)
canvas2.grid(row=1, column=6, columnspan=6, sticky=N, pady=2)
# Le bouton qui permet de quitter l'application.
bouton = Button(fenetre, text="Quit", fg="red", bg="white", relief="raised",
                overrelief="sunken", command=fenetre.destroy)
bouton.grid(row=3, column=0, columnspan=12, sticky=N+W+E, pady=2)





fenetre.mainloop()

