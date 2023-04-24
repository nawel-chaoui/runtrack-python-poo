class Animal:
    def __init__(self):
        self.prenom = ""
        self.age = 0

    def veillir(self):
        self.age += 1 

    def nommer(self, nom):
        self.prenom = nom

pet = Animal()
print("L'âge de l'animal est de", pet.age, "ans")

pet.veillir()
print("L'âge de l'animal est de", pet.age, "ans")

pet.nommer("Luna")
print("L'animal se somme",pet.prenom)