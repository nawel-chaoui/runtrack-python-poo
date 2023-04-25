class Rectangle:                               # création de la classe rectangle avec attributs privés longueur + largeur
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):                        # création de la méthode périmètre = calcul périmètre
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):                          # création de la méthode surface = calcule volume
        return self.__longueur * self.__largeur

    def get_longueur(self):                     # création getters = accesseurs
        return self.__longueur
    
    def set_longueur(self, longueur):           # création des setters = mutateurs
        self.__longueur = longueur
    
    def get_largeur(self):                      # création getters = accesseurs
        return self.__largeur 
    
    def set_largeur(self, largeur):             # création des setters = mutateurs
        self.__largeur = largeur

class Parallelepipede(Rectangle):               # création de la classe para' héritant de la classe rectangle
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur                # ajout de l'attribut hauteur

        def volume(self):                       # création de la méthode volume = calcule aire
         return self.surface() * self.__hauteur


# Instanciation de la classe rectangle + tests des méthodes
rectangle = Rectangle(5, 10)
print(rectangle.perimetre())  
print(rectangle.surface())  

rectangle.set_longueur(15)     # test mutateur
rectangle.set_largeur(20)      # test mutateur
print(rectangle.perimetre())  
print(rectangle.surface())  
