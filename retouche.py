from tkinter import *
from tkinter.messagebox import *
from PIL.Image import *
from PIL import Image, ImageTk
import random
# On crée la fenêtre principale avec un titre et un fond
fenetre = Tk()
fenetre.title("PhotoSturm")
fenetre['bg'] = '#FA8072'
class MonImage():

    def __init__(self, img):
        (L, H) = img.size
        self.img_origine = img
        self.hauteur = H
        self.longueur = L
        self.tkimage_origine = ImageTk.PhotoImage(img)
        self.tkimage_modif = ImageTk.PhotoImage(img)

    def info(self):
        print("Mon image a une hauteur de {} et une longueur de {}".format(self.hauteur, self.longueur))



CHEMIN = "image/pomme.jpg"
originale = open(CHEMIN)

mon_image= MonImage(originale)
mon_image.info()
(L, H) = originale.size
nouvelle_image = originale.copy()
image_originale = ImageTk.PhotoImage(originale)
image_nouvelle = ImageTk.PhotoImage(nouvelle_image)

def negatif(im):
    for i in range(H): # On parcours les lignes de pixels de l'image
        for j in range(L): # On parcours les pixels de la ligne i
            (r, v, b) = originale.getpixel((j, i))
            nouvelle_image.putpixel((j, i), (255 - r, 255 - v, 255 - b))
    nouvelle_image.save("image/negatif.jpg", "JPEG")
    variable.set("image/negatif.jpg")
    im.tkimage = ImageTk.PhotoImage(nouvelle_image)
    canvas2.itemconfig(1, image=im.tkimage)

def claire(n, im):
    for i in range(H):  # On parcours les lignes de pixels de l'image
        for j in range(L):  # On parcours les pixels de la ligne i
            (r, v, b) = originale.getpixel((j, i))
            nouvelle_image.putpixel((j, i), (r + n, v + n, b + n))
    nouvelle_image.save("image/plusclair.jpg", "JPEG")
    variable.set("image/plusclair.jpg")
    im.tkimage = ImageTk.PhotoImage(nouvelle_image)
    canvas2.itemconfig(1, image=im.tkimage)


def sombre(im):
    for i in range(H):  # On parcours les lignes de pixels de l'image
        for j in range(L):  # On parcours les pixels de la ligne i
            (r, v, b) = originale.getpixel((j, i))
            nouvelle_image.putpixel((j, i), (r - 50, v - 50, b - 50))
    nouvelle_image.save("image/plussombre.jpg", "JPEG")
    im.tkimage = ImageTk.PhotoImage(nouvelle_image)
    canvas2.itemconfig(1, image=im.tkimage)


# On crée un petit label
# On crée les titres des deux parties principale de l'appli
titre_depart = Label(fenetre, text="Image de départ", padx=10)
titre_depart.grid(row=0, column=0, columnspan=6, sticky=N, pady=2, padx=5)
titre_fin = Label(fenetre, text="Image modifiée", padx=10)
titre_fin.grid(row=0, column=6, columnspan=6, sticky=N, pady=2, padx=5)
# Les boutons
bouton_negatif = Button(fenetre, text="Négatif", command=lambda: negatif(mon_image))
bouton_negatif.grid(row=2, column=0, sticky=N, pady=2)
bouton_clair = Button(fenetre, text="Plus clair", command=lambda: claire(200, mon_image))
bouton_clair.grid(row=2, column=1, sticky=N, pady=2)
bouton_sombre = Button(fenetre, text="Plus sombre", command=lambda: sombre(mon_image))
bouton_sombre.grid(row=2, column=2, sticky=N, pady=2)
bouton_save = Button(fenetre, text="Enregistrer", command=negatif, bg = 'green')
bouton_save.grid(row=2, column=8, sticky=N, pady=2)
# Un input
variable = StringVar()
variable.set(CHEMIN)
entre = Entry(fenetre, textvariable=variable, width=50, bg = '#999999', fg='blue')
entre.grid(row=2, column=6, sticky=W, pady=2)

# Les images
canvas = Canvas(fenetre, width=400, height=400)
canvas.create_image(50, 5, anchor=NW, image=image_originale)
canvas.grid(row=1, column=0, columnspan=6, sticky=N, pady=2)

canvas2 = Canvas(fenetre, width=400, height=400)
i = canvas2.create_image(0, 0, anchor=NW, image=image_nouvelle)
canvas2.grid(row=1, column=6, columnspan=6, sticky=N, pady=2)

# Le bouton qui permet de quitter l'application.
bouton = Button(fenetre, text="Quit", fg="red", bg="white", relief="raised",
                overrelief="sunken", command=fenetre.destroy)
bouton.grid(row=3, column=0, columnspan=12, sticky=N+W+E, pady=2)


fenetre.mainloop()

