import numpy as np
import random
from variables import *

def realizar_disparo(tablero, disparo=None, aleatorio=False):
    acierto = False
    
    # Si es aleatorio, generamos las coordenadas aquí mismo
    if aleatorio:
        disparo = (random.randint(0, DIMENSIONES_TABLERO - 1), 
                   random.randint(0, DIMENSIONES_TABLERO - 1))

    match tablero.tablero[disparo]:
        case "CARACTER_BARCO":
            tablero.tablero[disparo] = "CARACTER_IMPACTO"
            acierto = True
            print("¡Tocado!")
        case "CARACTER_AGUA":
            tablero.tablero[disparo] = "CARACTER_FALLO"
            print("Agua.")
        case "CARACTER_IMPACTO", "CARACTER_FALLO":
            print("Ya has disparado aquí.")

    # Si dispara la máquina (aleatorio), mostramos nuestro tablero (oculto=False)
    # Si dispara el jugador, mostramos el del oponente (oculto=True)
    mostrar_tablero(tablero, oculto=not aleatorio)
    
    return acierto

def mostrar_tablero(tablero, oculto=False):
    print(tablero.id_player)
    
    if oculto:
    
        tablero_mostrar = np.where(tablero.tablero == "CARACTER_BARCO", " ", tablero.tablero)
    else:
        tablero_mostrar = tablero.tablero
        
    print(tablero_mostrar)
    print("******************************************")
