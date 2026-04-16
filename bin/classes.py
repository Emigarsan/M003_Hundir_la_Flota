
"""Clases principales para gestionar el tablero del juego."""

# Se importan las variables de variables.py y se cargan numpy y random
import numpy as np
import random
from variables import *

# Definir clase tablero:

class tablero:
    def __init__(self, boats:dict[int, int], id_player:str):
        """Inicializa un tablero de juego para un jugador.

        Args:
            boats: Diccionario con los barcos y su eslora.
            id_player: Identificador o nombre del jugador.
        """
        self.id_player = str(id_player) # Para almacenar el nombre del jugador
        self.boats = boats # Para almacenar el diccionario de los barcos y sus esloras
        self.posiciones = {} # Para almacenar las coordenadas de cada barco
        self.ocupadas = set() # Para almacenar las coordenadas ocupadas
        self.tablero = np.full((DIMENSIONES_TABLERO,DIMENSIONES_TABLERO), CARACTER_AGUA) # Para almacenar el tablero con los barcos


# Método de clase para generar coordenadas diferentes para cada barco:

    def generar_coordenadas(self, fila:int, col:int, eslora:int, orientacion:str):
        """Genera las coordenadas ocupadas por un barco según su orientación.

        Args:
            fila: Fila inicial del barco.
            col: Columna inicial del barco.
            eslora: Longitud del barco.
            orientacion: Dirección del barco, entre N, S, E u O.

        Returns:
            list[tuple[int, int]]: Lista de coordenadas del barco.
        """

        coords = [] # Lista con las coordenadas

        for i in range(eslora): # Dependiendo del número de eslora se generan más o menos posiciones

            if orientacion == "N":
                posicion_f, posicion_c = fila - i, col
            elif orientacion == "S":
                posicion_f, posicion_c = fila + i, col
            elif orientacion == "E":
                posicion_f, posicion_c = fila, col + i
            elif orientacion == "O":
                posicion_f, posicion_c = fila, col - i

            coords.append((posicion_f, posicion_c))

        return coords 


# Definir método de clase para colocar barcos:
    def colocar_barcos(self):
        """Coloca todos los barcos del jugador en posiciones aleatorias válidas.

        El método intenta ubicar cada barco sin que se salga del tablero ni se
        solape con otros barcos ya colocados.
        """

        for nombre, eslora in self.boats.items():

            for _ in range(50):  # intentos limitados

                fila = random.randint(0, DIMENSIONES_TABLERO - 1)
                col = random.randint(0, DIMENSIONES_TABLERO - 1)
                orientacion = random.choice(["N", "S", "E", "O"])

                coords = self.generar_coordenadas(fila, col, eslora, orientacion)

                # Validar solapamiento y posición
                valido = True

                for posicion_f, posicion_c in coords:

                    if not (0 <= posicion_f < DIMENSIONES_TABLERO and 0 <= posicion_c < DIMENSIONES_TABLERO):
                        valido = False
                        break

                    if (posicion_f, posicion_c) in self.ocupadas:
                        valido = False
                        break

                # Guardar las posiciones en el diccionario si son válidas
                if valido:

                    self.posiciones[nombre] = coords

                    for posicion_f, posicion_c in coords:
                        self.tablero[posicion_f][posicion_c] = CARACTER_BARCO
                        self.ocupadas.add((posicion_f, posicion_c))

                    break