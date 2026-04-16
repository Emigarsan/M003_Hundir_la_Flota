import variables as var
from classes import tablero
from funciones import *

import numpy as np
import random

# ============================================================
# HUNDIR LA FLOTA --- BUCLE PRINCIPAL
# ============================================================

def main():
    # Mensaje de bienvenida - SI HAY TIEMPO añadir mas f-string?
    print("=" * 50)
    print("   BIENVENIDO A HUNDIR LA FLOTA")
    print("=" * 50)
    print("\nReglas:")
    print(f"- Tablero de {var.DIMENSIONES_TABLERO}x{var.DIMENSIONES_TABLERO}")
    print("- Barcos: 1x4, 2x3, 3x2, 4x1")
    print("- Si tocas, repites turno")
    print("- Gana quien hunda todos los barcos del rival\n") 

    # Iniciar tableros para jugador y maquina, empieza siempre el jugador
    tablero_jugador = tablero(var.BARCOS, var.NOMBRES_JUGADORES[0])
    tablero_maquina = tablero(var.BARCOS, var.NOMBRES_JUGADORES[1])

    tablero_jugador.colocar_barcos()
    tablero_maquina.colocar_barcos()

    # Bucle de juego - al jugador le imprime un mensaje y pide el input, lo valida, y repite el el turno mientras realizar_disparo devuelva True
    #                   la maquina simplemente dispara aleatoriamente mientras sea su turno
    while True:

        # ---- TURNO DEL JUGADOR ----
        if var.TU_TURNO:
            print("\n>>> TURNO DEL JUGADOR <<<")
            mostrar_tablero(tablero_jugador)
            mostrar_tablero(tablero_maquina, oculto = var.OCULTO)
            # pedir_coordenadas deberia llamarse desde funciones.py 
            disparo = pedir_coordenadas()

            # Validar que el disparo no sea repe
            if casilla_ya_disparada(tablero_maquina, disparo):
                print("Ya has disparado en esa casilla. Elige otra.")
            else:
                # Realiza el disparo
                tocado = realizar_disparo(tablero_maquina, disparo)
                mostrar_tablero(tablero_maquina, oculto = var.OCULTO)
                # comprobar_fin deberia estar en funciones.py
                if comprobar_fin(tablero_maquina):
                    print("\nHas hundido toda la flota enemiga!")
                    print("VICTORIA DEL JUGADOR!")
                    break
                # Si tocado es True, repite turno. De lo contrario, acaba.
                if tocado:
                    print("Repites turno.")
                else:
                    var.TU_TURNO = False

                pausa=input("Presiona Enter para continuar...")

        # ---- TURNO DE LA MAQUINA ----
        else:
            print("\n>>> TURNO DE LA MAQUINA <<<")
            # TODO Ahora mismo la maquina no sabe que no debe no repetir disparos 
            disparo_maquina = coordenadas_aleatorias(var.DIMENSIONES_TABLERO)
             # Validar que el disparo no sea repe
            if casilla_ya_disparada(tablero_jugador, disparo_maquina):
                print("Ya has disparado en esa casilla. Elige otra.")
            else:
                tocado = realizar_disparo(tablero_jugador, disparo_maquina)
                mostrar_tablero(tablero_jugador)
                # comprobar_fin deberia estar en funciones.py
                if comprobar_fin(tablero_jugador):
                    print("\nLa maquina ha hundido toda tu flota...")
                    print("DERROTA.")
                    break
                # Si tocado es True, repite turno. De lo contrario, acaba.
                if tocado:
                    print("La maquina repite turno.")
                else:
                    var.TU_TURNO = True

    # Mensaje de fin de partida
    print("\n--- TABLERO FINAL ---")
    mostrar_tablero(tablero_jugador)
    mostrar_tablero(tablero_maquina)
    print("\nGracias por jugar a Hundir la Flota!")


if __name__ == "__main__":
    main()
