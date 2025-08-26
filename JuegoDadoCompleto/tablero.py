import time
from dado import animacion_dado, limpia_console

class Tablero:
    def __init__(self, casillas=15):
        self.casillas = casillas

    def jugar(self, jugadores):
        print(f"\n🎯 Comienza la carrera hasta la casilla {self.casillas}!\n")
        ganador = None

        # Bucle principal del juego
        while not ganador:
            # Ordenamos por turno (definido en main.py con la tirada inicial)
            for jugador in sorted(jugadores, key=lambda x: x.turno):
                limpia_console()
                input(f"\n👉 Turno de {jugador.nombre}. Presiona ENTER para tirar el dado... ")
                tirada = animacion_dado()
                print(f"{jugador.nombre} sacó un {tirada}")

                # Avanza el jugador
                jugador.avanzar(tirada)
                jugador.mostrar_estado()
                time.sleep(1)

                # Comprobar si ganó
                if jugador.posicion >= self.casillas:
                    ganador = jugador
                    break

        print("\n" + "="*40)
        print(f"🏆 FELICIDADES {ganador.nombre}, GANASTE LA CARRERA 🎉🎉")
        print("="*40)
