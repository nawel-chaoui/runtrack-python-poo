# L'utilisation de getters et setters permet de contrôler l'accès aux attributs privés d'une classe, 
# ce qui peut être utile pour assurer l'encapsulation des données et la cohérence de l'état de l'objet.

class Rectangle :
    def __init__(self, longueur, largeur):
        self.__longueur = longueur    # __ pour les attributs privées
        self.__largeur =  largeur

    def get_longueur(self):  # get = getters, assesseur (permettant de récupérer la valeur d'un attribut privé)
        return self.__longueur

    def set_longueur(self,longueur):  # set = setters, mutateurs (permettant de modifier la valeur d'un attribut privé)
        self.__longueur =  longueur

    def get_largeur(self):
        return self.__largeur 

    def set_largeur(self, largeur):
        self.__largeur = largeur

figure = Rectangle(10, 5)
print("Premières valeurs longueur/largeur :",figure.get_longueur(), "et", figure.get_largeur())

figure.set_largeur(9)
figure.set_longueur(15)
print("Nouvelles valeurs longueur/largeur :", figure.get_longueur(), "et", figure.get_largeur())

