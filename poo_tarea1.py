"""
Alumno: Cristian Manuel Brambilla
1er año TUP

Este programa implementa un sistema básico de gestión de vehículos.

En primer lugar, se define la clase principal Vehiculo, que representa un objeto genérico con atributos comunes como marca, modelo, año, titular, patente y estado de venta (vendido).
También se implementan métodos como encender(), apagar(), andar() y especificaciones(), que representan acciones comunes para todos los vehículos.

Además, se incluye un método getter (get_titular) y un setter (set_titular) para acceder y modificar el titular del vehículo, 
condicionado por el atributo self.vendido (solo se puede cambiar el titular si el vehículo fue vendido).

Luego, se crean las clases derivadas Auto y Moto. Cada una agrega un nuevo atributo específico: 
Auto incluye la cantidad de puertas, mientras que Moto incluye la cilindrada. Ambas redefinen el método especificaciones() para mostrar su información extendida.

Finalmente, se realizan pruebas instanciando objetos de Auto y Moto, y utilizando los métodos definidos. 
Se recomienda descomentar y modificar las líneas de prueba según se desee para verificar el funcionamiento.
"""

class Vehiculo:
    def __init__(self, marca, modelo, anio, titular, patente, vendido):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.__titular = titular
        self.__patente = patente
        self.vendido = vendido

    # Métodos para mover vehículo
    def encender(self):
        print(f"{self.marca} {self.modelo} está encendido y listo para moverse...")
    def apagar(self):
        print(f"Se apagó {self.marca} {self.modelo}")
    def andar(self):
        print(f"{self.marca} {self.modelo} está andando")

    # Mostrar especificaciones
    def especificaciones(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Titular: {self.__titular}")
        print(f"Patente: {self.__patente}")
        print(f"Vendido: {self.vendido}")

    # GET para extraer el dato titular
    def get_titular(self):
        return self.__titular

    # SET para cambiar de titular del vehículo
    def set_titular(self, nuevo_titular):
        if self.vendido:
            self.__titular = nuevo_titular
            print(f"Ahora el vehículo pertenece a: {self.__titular}")
        else:
            print(f"El vehículo todavía pertenece a: {self.__titular}")

# Heredamos "Vehículo" y lo convertimos en AUTO
class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, titular, patente, vendido, puertas):
        super().__init__(marca, modelo, anio, titular, patente, vendido)
        self.puertas = puertas

    # Agregamos cantidad de puertas como nuevo atributo
    def especificaciones(self):
        print("El AUTO es:")
        super().especificaciones()
        print(f"Cantidad de puertas: {self.puertas}")
        print("-------------------------------------------------------")

    def encender(self):
        print(f"El {self.marca} {self.modelo} rugió al encender!")
        print("Aceléralo con cuidado...")
    def andar(self):
        print(f"El andar del {self.marca} {self.modelo} es muy confortable!")
    def apagar(self):
        print("Se apagó sin problemas, no te olvides las luces encendidas....")


# Heredamos "Vehículo" y lo convertimos en MOTO
class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, titular, patente, vendido, cilindrada):
        super().__init__(marca, modelo, anio, titular, patente, vendido)
        self.cilindrada = cilindrada

    # Agregamos como nuevo dato la cilindrada de la moto
    def especificaciones(self):
        print("La MOTO es:")
        super().especificaciones()
        print(f"Cilindrada: {self.cilindrada}")
        print("-------------------------------------------------------")

    def encender(self):
        print(f"La moto {self.marca} {self.modelo} encendió a la primer patada! Está lista para salir...")
    def andar(self):
        print(f"La {self.marca} {self.modelo} se mueve silenciosamennte!")
    def apagar(self):
        print(f"La moto se apagó sin problemas!")


# ==== Pruebas ====

mi_auto = Auto("Fiat", "147 Vivace", 1994, "Manuel Brambilla", "RNA 123", False, "3")
# mi_auto.especificaciones()
# mi_auto.set_titular("Marecelo Gallardo") #No deberia cambiar

mi_auto.vendido = True  # Marcamos el Auto como vendido
mi_auto.set_titular("Enzo Perez")
mi_auto.especificaciones()
mi_auto.encender()
mi_auto.andar()
mi_auto.apagar()

#mi_moto = Moto("Honda", "Wave", 2020, "Manuel Brambilla", "AA RNA 123", False, 125)
#mi_moto.especificaciones()
#mi_moto.encender()
#mi_moto.andar()
#mi_moto.apagar()