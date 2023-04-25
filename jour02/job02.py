class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print("J'ai", self.age, "ans")

    def bonjour(self):
        print("\033[1;32mHello\033[0m") # Ajout code couleur

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours(self):
        print("\033[1;33mJe vais en cours") # Ajout code couleur
    
    def afficherAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee, age):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("\033[1;33mLe cours va commencer.\033[0m") # Ajout code couleur

# Instanciation d'une personne et de l'élève
p = Personne()
e = Eleve()

# Faire dire bonjour à l'élève et aller en cours
e.bonjour()
e.allerEnCours()

# Redéfinir l'âge de l'élève à 15 ans
e.modifierAge(15)

# Instanciation du professeur
prof = Professeur("Développement web", 40)

# Faire dire bonjour au professeur et commencer le cours
prof.bonjour()
prof.enseigner()