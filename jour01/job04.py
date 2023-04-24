class Personne :
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}."

people1 = Personne("John", "Doe")
people2 = Personne("Jean","Dupond")

print(people1.SePresenter())
print(people2.SePresenter())