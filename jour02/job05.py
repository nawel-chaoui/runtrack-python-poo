class Forme:                     # création de la classe forme + méthode aire retournant 0
    def aire(self):
        return 0

class Cercle(Forme):             # création de la classe héritère de forme + création attribut radius
     def __init__(self,radius):
        self.radius = radius

class Rectangle(Forme):          # création de la classe rectangle hértant de la classe forme
    def __init__(self, largeur, hauteur):     # ajout de ses attributs largeur + hauteur
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur  # surcharge de la méthode aire afin qu'elle renvoie l'aire du rectangle

class Cercle(Forme):             # création de la classe héritère de forme + création attribut radius
    def __init__(self,radius):
        self.radius = radius
    
    def aire(self):              # # surcharge de la méthode aire afin qu'elle renvoie l'aire du cercle
        return 3.14 * self.radius ** 2  # 3.14 pour Pi

# instanciation + tests différentes valeurs et affichage
rectangle = Rectangle(10, 30)
print("\nL'aire du rectangle :",rectangle.aire())  # Renvoie 50

cercle = Cercle(10)
print("\nL'aire du cercle :",cercle.aire())  # Renvoie 78.5

rectangle = Rectangle(5, 15)
print("\nL'aire du rectangle :",rectangle.aire())  # Renvoie 50

cercle = Cercle(5)
print("\nL'aire du cercle :",cercle.aire())  # Renvoie 78.5