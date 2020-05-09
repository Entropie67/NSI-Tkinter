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
label2 = Label(frame2, text="Image modifiée")
label2.pack()

bouton_choix = Button(frame1, text="Négatif", command=negatif)
bouton_choix.pack(side = BOTTOM, padx = 10, pady = 10)

# on crée un bouton
bouton = Button(fenetre, text="Quit", command=fenetre.destroy)
bouton.pack(side=BOTTOM, expand = True, fill = BOTH, padx = 10, pady = 10)

# Un input
variable = StringVar()
variable.set(chemin)
entre = Entry(frame2, textvariable=variable, width=50, bg = '#999999', fg='blue')
entre.pack(side = BOTTOM, padx = 10, pady = 10)

image = ImageTk.PhotoImage(originale)
canvas = Canvas(frame1, width=400, height=400)
canvas.create_image(0,0, anchor=NW, image=image)
canvas.pack(side=RIGHT)

image2 = ImageTk.PhotoImage(Image.open("image/resultat.jpg"))

canvas2 = Canvas(frame2, width=400, height=400)
i =canvas2.create_image(0, 0, anchor=NW, image=image)
print(i)

canvas2.pack(side=RIGHT)


fenetre.mainloop()

