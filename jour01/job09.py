class Student:
    def __init__(self, prenom, nom, id):
        self.__prenom = prenom
        self.__nom = nom
        self.__id = id
        self.__credits = 0
        self.__level = self.__studentEval()

    def get_credits(self):
        return self.__credits 

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print("Nom: ", self.__nom)
        print("Prénom: ", self.__prenom)
        print("Identifiant: ", self.__id)    
        print("Niveau: ", self.__level)

# Instanciation de l'étudiant John Doe
john_doe = Student("John", "Doe", 145)
print()

# Ajout de crédits à l'étudiant John Doe
john_doe.add_credits(30)
john_doe.add_credits(20)
john_doe.add_credits(25)

# Affichage des informations de l'étudiant John Doe
print("Le nombre de crédits de John Doe est de", john_doe.get_credits())
john_doe.studentInfo()