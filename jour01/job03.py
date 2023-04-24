class operation:
    def __init__(self, nombre1=5, nombre2=5):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(resultat)

ope = operation()
ope.addition()