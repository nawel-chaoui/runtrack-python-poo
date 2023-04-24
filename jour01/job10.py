class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.en_marche = False
        self.__reservoir = 50

# Getters et setters
    def get_marque(self):
        return self.marque
    def set_marque(self, marque):
        self.marque = marque

    def get_modele(self):
        return self.modele
    def set_modele(self, modele):
        self.modele = modele

    def get_annee(self):
        return self.annee
    def set_annee(self, annee):
        self.annee = annee

    def get_kilometrage(self):
        return self.kilometrage
    def set_kilometrage(self, kilometrage):
        self.kilometrage = kilometrage

# Méthode "démarrer" et "arrêter" changeant l'attribut en_marche
    def get_en_marche(self):
        return self.en_marche

    def demarrer(self):
        if self.__verifier_plein__():
            self.en_marche = True
            print("La voiture démarre.")
        else:
            print("Le réservoir est presque vide. Impossible de démarrer.")

    def arreter(self):
        self.en_marche = False
        print("La voiture s'arrête.")

# Méthode privé verifier_plein qui retourne l'attribut reservoir
    def get_reservoir(self):
        return self.__reservoir

    def __verifier_plein__(self):
        if self.__reservoir > 5:
            return True
        else:
            return False

# Instanciation de l'objet voiture
voiture1 = Voiture("Renault", "Clio", 2020, 20000)

# Modification des attributs
voiture1.set_marque("Peugeot")
voiture1.set_modele("308")
voiture1.set_annee(2022)
voiture1.set_kilometrage(5000)

# Appel des méthodes de la voiture
voiture1.demarrer()
voiture1.arreter()

# Affichage des résultats
print("Marque : ", voiture1.get_marque())
print("Modèle : ", voiture1.get_modele())
print("Année : ", voiture1.get_annee())
print("Kilométrage : ", voiture1.get_kilometrage())
print("En marche : ", voiture1.get_en_marche())
print("Réservoir : ", voiture1.get_reservoir())