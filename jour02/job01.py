class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge (self):
        print(self.age, "ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print("J'ai", self.age, "ans")

class Professeur:
    def __init__(self, matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée
    
    def enseigner(self):
        print("Le cours va commencer.")

# Instanciation d'une personne et d'un élève
p = Personne()
e = Eleve()

# Affichage de l'âge de l'élève par défaut
e.afficherAge()