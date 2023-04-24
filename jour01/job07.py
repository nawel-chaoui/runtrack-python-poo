class Livre : 
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages =  pages
    
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
    def set_pages(self, nb_pages):
        self.__pages = pages

LeLivre = Livre("Le lapin de lune", "Alain Gerber", 300)
print(LeLivre.get_titre(),"de",LeLivre.get_auteur(),"fait",LeLivre.get_pages(),"pages.")