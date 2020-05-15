
class MonImage():
    def __init__(self, img, img_tk):
        (L, H) = img.size
        self.img_origine = img
        self.hauteur = H
        self.longueur = L
        self.tkimage_origine = img_tk
        self.tkimage_modif = img_tk

    def info(self):
        print("Mon image a une hauteur de {} et une longueur de {}".format
            (self.hauteur, self.longueur))

