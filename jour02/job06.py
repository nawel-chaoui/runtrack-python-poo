class Vehicule:                                   # création de la classe véhicule + ses attributs
    def __init__(self, marque, modèle, année, prix):
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix

    def informationsVehicule(self):               # création de la méthode info'véhicule qui écrit en console les attributs
        print("\nMarque :", self.marque)
        print("Modèle :", self.modèle)
        print("Année :", self.année)
        print("Prix :", self.prix)

class Voiture(Vehicule):                          # création de la classe voiture héritière de véhicule
    def __init__(self, marque, modèle, année, prix):
        super().__init__(marque, modèle, année, prix)  # appel contructeur classe parente avec les mêmes attributs
        self.portes = 4          # ajout de l'attribut porte

    def informationsVehicule(self):  # création méthode 
        super().informationsVehicule()
        print("Nombre de portes :", self.portes)

class Moto(Vehicule):                           # création de la classe moto héritière de véhicule
    def __init__(self, marque, modèle, année, prix):  
        super().__init__(marque, modèle, année, prix) # appel contructeur classe parente avec les mêmes attributs
        self.roues = 2  # ajout de l'attribut roues
        
    def informationsVehicule(self):  # création méthode
        super().informationsVehicule()
        print("Nombre de roues :", self.roues)
        

# instanciation objet voiture + affichage de la méthode info'véhicule
voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
voiture.informationsVehicule()  

# instanciation objet moto + affichage de la méthode info'véhicule
moto = Moto("Yamaha", "1200 VMAX", 1987, 4500)
moto.informationsVehicule()