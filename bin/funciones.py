"""Funciones auxiliares para disparar y mostrar el tablero."""

import numpy as np
import random
import variables as var

def coordenadas_aleatorias(dim_tablero):
    """Genera coordenadas aleatorias dentro de las dimensiones del tablero.

    Args:
        dim_tablero: Tamaño del tablero (n x n).

    Returns:
        tuple[int, int]: Coordenadas generadas (fila, columna).
    """
    fila = random.randint(0, dim_tablero - 1)
    columna = random.randint(0, dim_tablero - 1)
    return (fila, columna)

def realizar_disparo(tablero, disparo:tuple[int, int]=None):
    """Ejecuta un disparo sobre un tablero y muestra el resultado.

    Args:
        tablero: Instancia del tablero objetivo.
        disparo: Tupla con la posición a disparar.

    Returns:
        bool: True si el disparo impacta en un barco, False en caso contrario.
    """
    acierto = False

    match tablero.tablero[disparo]:
        case var.CARACTER_BARCO:
            tablero.tablero[disparo] = var.CARACTER_IMPACTO
            acierto = True
            print("¡Tocado!")
        case var.CARACTER_AGUA:
            tablero.tablero[disparo] = var.CARACTER_FALLO
            print("Agua.")
        case var.CARACTER_IMPACTO, var.CARACTER_FALLO:
            print("Ya has disparado aquí.")

    # Si dispara la máquina (aleatorio), mostramos nuestro tablero (oculto=False)
    # Si dispara el jugador, mostramos el del oponente (oculto=True)
    # mostrar_tablero(tablero, oculto=not aleatorio)
    
    return acierto

def mostrar_tablero(tablero, oculto:bool=False):
    """Muestra el tablero por pantalla, ocultando los barcos si procede.

    Args:
        tablero: Instancia del tablero a mostrar.
        oculto: Si es True, oculta las posiciones de los barcos.
    """

    print(tablero.id_player)
    
    if oculto:
    
        tablero_mostrar = np.where(tablero.tablero == var.CARACTER_BARCO, " ", tablero.tablero)
    else:
        tablero_mostrar = tablero.tablero
        
    print(tablero_mostrar)
    print("\n******************************************")

# Para pedir el input al jugador y validar que esta dentro de rango 0-TABLERO y sea tipo int
def pedir_coordenadas():

    while True:
        try:
            fila = int(input(f"Fila (0-{var.DIMENSIONES_TABLERO - 1}): "))
            columna = int(input(f"Columna (0-{var.DIMENSIONES_TABLERO - 1}): "))
            if 0 <= fila < var.DIMENSIONES_TABLERO and 0 <= columna < var.DIMENSIONES_TABLERO:
                return (fila, columna)
            print("Coordenadas fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Introduce un numero valido.")

# Comprueba que se no haya disparado ya a esa celda. 

def casilla_ya_disparada(tab, disparo):
    return tab.tablero[disparo] in (var.CARACTER_IMPACTO, var.CARACTER_FALLO)

# Recorre tablero para comprobar si queda algun barco vivo 
# barco vivo = casilla no es agua (" "), impacto ("X") ni fallo ("-")

def comprobar_fin(tab):
    for fila in tab.tablero:
        for casilla in fila:
            if casilla not in (" ", var.CARACTER_IMPACTO, var.CARACTER_FALLO):
                return False
    return True