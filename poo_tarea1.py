class Personaje:
    def __init__(self, nombre, def_fis, def_mag, fuerza, inteligencia, vida, arma):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.def_fis = def_fis
        self.def_mag = def_mag
        self.vida = vida
        self.arma = arma
#ATRIBUTOS PERSONAJE
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Defensa Física:", self.def_fis)
        print("-Defensa Mágica:", self.def_mag)
        print("-Vida:", self.vida)
        print("-Arma:", self.arma)
#ACCIONES
    def subir


manu = Personaje()
print(manu)