class Vehiculo:
    def __init__(self, marca, modelo, anio, titular, patente, vendido):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.__titular = titular
        self.__patente = patente
        self.vendido = vendido

# Métodos para mover vehículo
    def __encender(self):
        print(f"{self.marca} {self.modelo} está encendido y listo para moverse...")

    def __apagar(self):
        print(f"Se apagó {self.marca} {self.modelo}")

    def __andar(self):
        print(f"{self.marca} {self.modelo} está andando")

#Mostrar especificaciones 
    def especificaciones(self):
        #print(f"El vehículo seleccionado es:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Titular: {self.__titular}")
        print(f"Patente: {self.__patente}")
        print(f"Vendido: {self.vendido}")

    def se_vende(self):
#Modificar titular, GET para extraer el dato
        def get_titular(self):
            return self.__titular
#En caso de self.vendido cambie a TRUE, el titular va a cambiar, si no seguirá con el mismo dato declarado con el objeto. 
        def set_titular(self, titular):
            if self.vendido == False:
                print(f"El vehículo todavía pertenece a: {self.__titular}")
            else:
                self.__titular = titular
                print(f"Ahora el vehículo pertenece a: {self.__titular}")


#Heredamos "Vehículo" y lo convertimos en AUTO
class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, titular, patente, vendido, puertas):
        super().__init__(marca, modelo, anio, titular, patente, vendido)
        self.puertas = puertas
    #Agregamos cantidad de puertas como nuevo atributo para autos
    def especificaciones(self):
        print("El AUTO es:")
        super().especificaciones()
        print(f"Cantidad de puertas: {self.puertas}")
        print("-------------------------------------------------------")

#Heredamos "Vehículo" y lo convertimos en MOTO
class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, titular, patente, vendido, cilindrada):
        super().__init__(marca, modelo, anio, titular, patente, vendido)
        self.cilindrada = cilindrada
    #Agregamos como nuevo dato la cilindrada de la moto
    def especificaciones(self):
        print("La MOTO es:")
        super().especificaciones()
        print(f"Cilindrada: {self.cilindrada}")
        print("-------------------------------------------------------")

mi_auto = Auto("Fiat", "147 Vivace", 1994, "Manuel Brambilla", "RNA 123", False, "3")
mi_auto.especificaciones()

mi_auto = Auto("Fiat", "147 Vivace", 1994, "RORO Lopez", "RNA 123", True, "3") #Cambio a TRUE el atributo VENDIDO
mi_auto.especificaciones()



mi_moto = Moto("Honda", "Wave", 2020, "Manuel Brambilla", "AA RNA 123", False, 125)
mi_moto.especificaciones()