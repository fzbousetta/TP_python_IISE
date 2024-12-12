class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur

    def calculer_perimetre(self):
        return 2 * (self.largeur + self.hauteur)


rectangle1 = Rectangle(5,10)
surface = rectangle1.calculer_surface()
perimetre = rectangle1.calculer_perimetre()

print(surface)
print(perimetre)