import variables as var
from classes import tablero
from funciones import *

import numpy as np
import random
import time

# ============================================================
# HUNDIR LA FLOTA --- BUCLE PRINCIPAL
# ============================================================

def main() -> None:
    """Función principal que ejecuta el bucle de juego.

    Inicializa dos tableros (jugador vs máquina), posiciona los barcos
    de ambos jugadores y controla el bucle principal de turnos hasta
    determinar un ganador.
    """
    # Mensaje de bienvenida 
    print("=" * 50)
    print("\tBIENVENIDO A HUNDIR LA FLOTA")
    print("=" * 50)
    print("\nReglas:")
    print(f"- Tablero de {var.DIMENSIONES_TABLERO}x{var.DIMENSIONES_TABLERO}")
    print("- Barcos: 1x4, 2x3, 3x2, 4x1")
    print("- Si tocas, repites turno")
    print("- Gana quien hunda todos los barcos del rival\n") 

    # Inicializa un tablero para cada jugador con la configuración de barcos
    tablero_jugador = tablero(var.BARCOS, var.NOMBRES_JUGADORES[0])
    tablero_maquina = tablero(var.BARCOS, var.NOMBRES_JUGADORES[1])

    # Posiciona todos los barcos de forma aleatoria en ambos tableros
    tablero_jugador.colocar_barcos()
    tablero_maquina.colocar_barcos()

    # Bucle principal de juego: continúa hasta que algún jugador hunda toda la flota enemiga
    while True:

        # ---- TURNO DEL JUGADOR HUMANO ----
        if var.TU_TURNO:
            print("\n>>> TURNO DEL JUGADOR <<<\n")
            # Muestra el tablero propio y el del oponente (ocultando barcos si es necesario)
            mostrar_tablero(tablero_jugador)
            mostrar_tablero(tablero_maquina, oculto = var.OCULTO)
            time.sleep(0.5)
            
            # Solicita al jugador que ingrese coordenadas para el disparo
            disparo = pedir_coordenadas()
            repetida = True
            
            # Valida repetidamente que el disparo no haya sido realizado previamente
            while repetida:
                # Comprueba si la casilla ya fue impactada o marcada como fallo
                repetida = casilla_ya_disparada(tablero_maquina, disparo)

                if repetida:
                    print("\nYa has disparado en esa casilla. Elige otra.")
                    disparo = pedir_coordenadas()
                else:
                    # Ejecuta el disparo en el tablero enemigo
                    tocado = realizar_disparo(tablero_maquina, disparo)
                    mostrar_tablero(tablero_maquina, oculto = var.OCULTO)
                    
                    # Evalúa si la flota enemiga ha sido completamente hundida
                    if comprobar_fin(tablero_maquina):
                        print("\nHas hundido toda la flota enemiga!")
                        print("VICTORIA DEL JUGADOR!")
                        break
                    
                    # Lógica de turno: acierto = repetir; fallo = pasar turno a máquina
                    if tocado:
                        print("\nRepites turno.")
                    else:
                        var.TU_TURNO = False

                    pausa = input("\nPresiona Enter para continuar...\n")

        # ---- TURNO DE LA MÁQUINA ----
        else:
            print("\n>>> TURNO DE LA MAQUINA <<<")
            repetida = True
            while repetida:
                # Genera coordenadas aleatorias para el disparo de la máquina
                disparo_maquina = coordenadas_aleatorias(var.DIMENSIONES_TABLERO)
                repetida = casilla_ya_disparada(tablero_jugador, disparo_maquina)
            # Valida que la máquina no dispare a una casilla ya impactada
                if repetida:
                    # En caso de repetición, intenta nuevamente generar coordenadas válidas
                    print("La máquina intenta disparar a una casilla ya visitada.")
                else:
                    # Ejecuta el disparo de la máquina contra el tablero del jugador
                    tocado = realizar_disparo(tablero_jugador, disparo_maquina)
                    mostrar_tablero(tablero_jugador)
                    time.sleep(1)
                    
                    # Evalúa si la flota del jugador ha sido completamente hundida
                    if comprobar_fin(tablero_jugador):
                        print("\nLa máquina ha hundido toda tu flota...")
                        print("¡DERROTA! :(")
                        break
                        # Lógica de turno: acierto = repetir; fallo = pasar turno al jugador
                    if tocado:
                        print("\nLa maquina repite turno.")
                    else:
                        var.TU_TURNO = True
                time.sleep(1)
    # Visualización del estado final de ambos tableros
    print("\n--- TABLERO FINAL ---")
    mostrar_tablero(tablero_jugador)
    time.sleep(3)
    mostrar_tablero(tablero_maquina)
    time.sleep(3)
    print("\nGracias por jugar a Hundir la Flota!")


if __name__ == "__main__":
    main()
