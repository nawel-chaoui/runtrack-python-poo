class Forme:                     # création de la classe forme + méthode aire retournant 0
    def aire(self):
        return 0

class Rectangle(Forme):          # création de la classe rectangle hértant de la classe forme
    def __init__(self, largeur, hauteur):     # ajout de ses attributs largeur + hauteur
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur  # surcharge de la méthode aire afin qu'elle renvoie l'aire du rectangle

# instanciation 
rectangle1 = Rectangle(10, 30)
aire_rectangle1 = rectangle1.aire()

# affichage du résultat
print(aire_rectangle1)