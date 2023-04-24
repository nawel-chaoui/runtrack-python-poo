class Livre : 
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages =  pages
        self.__disponible =  True

    def get_titre(self):
        return self.__titre
    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur
    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_pages(self):
        return self.__pages
    def set_pages(self, pages):
        self.__pages = pages

    def verification(self):
        if self.__disponible == True:
            return("Disponible")
        if self.__disponible == False:
            return("Indisponible")

    def emprunter(self):
        check = self.verification()
        if check == "Disponible":
            print("Livre emprunté avec succés.")
            self.__disponible=False
        else:
            print("Livre déjà emprunté.")
            self.__disponible=True
    
    def rendre(self):
        check = self.verification()
        if check == "Indisponible":
            print("Livre rendu avec succés.")
            self.__disponible = True
        else:
            print("Livre déjà rendu.")

livre1 = Livre("Le lapin de lune", "Alain Gerber", 300)
livre2 = Livre("Blablabla","Toto", 250)

# test
print(livre1.get_titre(),"de",livre1.get_auteur(),"faisant",livre1.get_pages(),"pages.")
livre1.emprunter()
livre1.rendre()

print(livre2.get_titre(),"de",livre2.get_auteur(),"faisant",livre2.get_pages(),"pages.")
livre2.emprunter()
livre2.emprunter()

