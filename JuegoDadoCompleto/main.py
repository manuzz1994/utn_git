import time
from personaje import Personaje
from dado import animacion_dado
from tablero import Tablero

def main():
    print("Bienvenido al juego de los DADOS!!")
    print("====================================")
    print("El primero en llegar a la meta GANA!")
    print("====================================")

    # === Definir cantidad de jugadores ===
    while True:
        try:
            cantidad_jugadores = int(input("Ingrese cantidad de jugadores (de 2 a 4): "))
            if 2 <= cantidad_jugadores <= 4:
                break
            else:
                print("⚠ Debes ingresar un número entre 2 y 4.")
        except ValueError:
            print("⚠ Ingrese un número válido.")

    # === Crear lista de jugadores ===
    jugadores = []
    for jugador in range(cantidad_jugadores):
        nombre = input(f"Ingrese el nombre del jugador {jugador+1}: ").strip()
        while not nombre:
            nombre = input("El nombre no puede estar vacío. Intente nuevamente: ").strip()
        jugadores.append(Personaje(nombre, turno=0))

    # === Tirada inicial para decidir orden ===
    print("\nTirada inicial para decidir quién comienza...")
    tiradas = []
    for jugador in jugadores:
        print(f"\nTirada de {jugador.nombre}:")
        time.sleep(1)
        tirada = animacion_dado()
        print(f"{jugador.nombre} sacó un {tirada}")
        tiradas.append((jugador, tirada))
        time.sleep(1)

    # Ordenar de mayor a menor
    tiradas.sort(key=lambda x: x[1], reverse=True)

    # Asignar turnos
    print("\nOrden de los turnos:")
    for idx, (jugador, valor) in enumerate(tiradas, start=1):
        jugador.turno = idx
        print(f"{idx}. {jugador.nombre} (sacó {valor})")

    # === Crear tablero y jugar ===
    tablero = Tablero(casillas=15)   # cambiá a 10 o 20 si querés
    tablero.jugar(jugadores)


if __name__ == "__main__":
    main()
