import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"
    
class Jeu:
    def __init__(self):
        valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        couleurs = ["Coeur", "Carreau", "Pique", "Trèfle"]
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
    
    def melanger(self):
        random.shuffle(self.paquet)
    
    def donner_carte(self):
        return self.paquet.pop()
    
class Main:
    def __init__(self):
        self.cartes = []
    
    def ajouter_carte(self, carte):
        self.cartes.append(carte)
    
    def valeur(self):
        valeurs = {"As": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Valet": 10, "Dame": 10, "Roi": 10}
        valeur_main = sum(valeurs[carte.valeur] for carte in self.cartes)
        as_main = sum(carte.valeur == "As" for carte in self.cartes)
        while as_main > 0 and valeur_main > 21:
            valeur_main -= 10
            as_main -= 1
        return valeur_main
    
    def __repr__(self):
        return str(self.cartes)
    
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = Main()
    
    def ajouter_carte(self, carte):
        self.main.ajouter_carte(carte)
    
    def montrer_main(self):
        print(f"{self.nom}: {self.main}, valeur: {self.main.valeur()}")
    
class Croupier:
    def __init__(self):
        self.nom = "\nCroupier"
        self.main = Main()
    
    def ajouter_carte(self, carte):
        self.main.ajouter_carte(carte)
    
    def montrer_main(self):
        print(f"{self.nom}: {self.main.cartes[0]}, caché")
    
    def montrer_tout(self):
        print(f"{self.nom}: {self.main}, valeur: {self.main.valeur()}")
    
def jouer():
    jeu = Jeu()
    jeu.melanger()
    
    joueur = Joueur(input("\nEntrez votre nom: "))
    croupier = Croupier()
    
    joueur.ajouter_carte(jeu.donner_carte())
    croupier.ajouter_carte(jeu.donner_carte())
    joueur.ajouter_carte(jeu.donner_carte())
    croupier.ajouter_carte(jeu.donner_carte())
    
    croupier.montrer_main()
    joueur.montrer_main()
    
    while joueur.main.valeur() < 21:
        choix = input("\nVoulez-vous prendre une carte ? (o/n): ")
        if choix.lower() == "o":
            joueur.ajouter_carte(jeu.donner_carte())
            joueur.montrer_main()
        else:
            break
    
    croupier.montrer_tout()
    while croupier.main.valeur() < 17:
        croupier.ajouter_carte(jeu.donner_carte())
        croupier.montrer_tout()
    
    if joueur.main.valeur() > 21:
        print(f"\n{joueur.nom} a dépassé 21. Croupier gagne.")
    elif croupier.main.valeur() > 21:
        print(f"\nCroupier a dépassé 21. {joueur.nom} gagne.")
    elif joueur.main.valeur() > croupier.main.valeur():
        print(f"\n{joueur.nom} gagne.")
    elif joueur.main.valeur() < croupier.main.valeur():
        print("\nCroupier gagne.")
    else:
        print("\nMatch nul.")
    
jouer()