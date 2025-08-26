class Personaje:
    def __init__(self, nombre, turno):
        self.nombre = nombre
        self.turno = turno
        self.posicion = 0

    def avanzar(self, cantidad):
        self.posicion += cantidad
        if self.posicion > 15:
            self.posicion = 15  # No puede pasar la última casilla

    def mostrar_estado(self):
        print(f"{self.nombre} está en la casilla {self.posicion}")