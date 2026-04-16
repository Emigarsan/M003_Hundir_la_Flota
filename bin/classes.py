
"""Definición de la clase Tablero para gestionar el estado del juego.

Módulo que implementa la clase Tablero, responsable de:
- Inicializar el estado del tablero de juego
- Posicionar barcos de forma aleatoria y validada
- Gestionar el estado del tablero durante la partida
"""

import numpy as np
import random
from variables import *

class tablero:
    """Representa el tablero de juego de un jugador.
    
    Gestiona el posicionamiento y estado de los barcos, así como el registro
    de impactos y fallos durante la partida.
    """
    
    def __init__(self, boats:dict[int, int], id_player:str):
        """Inicializa un tablero de juego limpio para un jugador.

        Args:
            boats (dict): Índice de barcos disponibles con su eslora (nombre -> longitud).
            id_player (str): Identificador único del propietario del tablero.
        """
        # Identificador del jugador propietario de este tablero
        self.id_player = str(id_player)
        
        # Referencia a la configuración de barcos disponibles (nombre -> eslora)
        self.boats = boats
        
        # Diccionario que mapea nombres de barcos a sus coordenadas ocupadas
        self.posiciones = {}
        
        # Conjunto de coordenadas ocupadas (para validación rápida de solapamientos)
        self.ocupadas = set()
        
        # Matriz NumPy 10x10 que representa el estado actual del tablero
        self.tablero = np.full((DIMENSIONES_TABLERO, DIMENSIONES_TABLERO), CARACTER_AGUA)


# Método de clase para generar coordenadas diferentes para cada barco:

    def generar_coordenadas(self, fila:int, col:int, eslora:int, orientacion:str) -> list[tuple[int, int]]:
        """Genera las coordenadas ocupadas por un barco según orientación y eslora.

        Calcula la secuencia de celdas que ocupa un barco a partir de su posición
        inicial y dirección de crecimiento.

        Args:
            fila (int): Coordenada de fila inicial (0-9).
            col (int): Coordenada de columna inicial (0-9).
            eslora (int): Longitud del barco en celdas (1-4).
            orientacion (str): Dirección del barco: 'N' (norte), 'S' (sur), 
                             'E' (este), 'O' (oeste).

        Returns:
            list[tuple[int, int]]: Lista de coordenadas (fila, columna) ocupadas.
        """
        coords = []  # Acumulador de coordenadas del barco

        # Itera eslora veces para generar todas las celdas del barco
        for i in range(eslora):
            # Calcula la posición según la orientación
            if orientacion == "N":
                # Dirección norte: disminuye fila
                posicion_f, posicion_c = fila - i, col
            elif orientacion == "S":
                # Dirección sur: aumenta fila
                posicion_f, posicion_c = fila + i, col
            elif orientacion == "E":
                # Dirección este: aumenta columna
                posicion_f, posicion_c = fila, col + i
            elif orientacion == "O":
                # Dirección oeste: disminuye columna
                posicion_f, posicion_c = fila, col - i

            coords.append((posicion_f, posicion_c))

        return coords 


# Definir método de clase para colocar barcos:
    def colocar_barcos(self) -> None:
        """Posiciona todos los barcos del jugador en el tablero de forma aleatoria.

        Utiliza un algoritmo de búsqueda aleatoria con reintentos para posicionar
        cada barco. Valida que no salga del tablero ni se solape con barcos previos.
        """
        # Itera sobre cada barco definido en la configuración
        for nombre, eslora in self.boats.items():
            # Máximo de intentos para posicionar cada barco
            for intento in range(50):
                # Genera coordenada inicial aleatoria dentro del tablero
                fila = random.randint(0, DIMENSIONES_TABLERO - 1)
                col = random.randint(0, DIMENSIONES_TABLERO - 1)
                
                # Selecciona orientación aleatoria: N (norte), S (sur), E (este), O (oeste)
                orientacion = random.choice(["N", "S", "E", "O"])

                # Calcula todas las coordenadas que ocuparía el barco
                coords = self.generar_coordenadas(fila, col, eslora, orientacion)

                # Validación: verifica que todos los puntos estén dentro del tablero
                # y que no se solapan con barcos existentes
                valido = True

                for posicion_f, posicion_c in coords:
                    # Comprobación de límites del tablero
                    if not (0 <= posicion_f < DIMENSIONES_TABLERO and 0 <= posicion_c < DIMENSIONES_TABLERO):
                        valido = False
                        break

                    # Comprobación de solapamiento con barcos ya colocados
                    if (posicion_f, posicion_c) in self.ocupadas:
                        valido = False
                        break

                # Si la posición es válida, registra el barco y pasa al siguiente
                if valido:
                    # Almacena las coordenadas del barco para referencia posterior
                    self.posiciones[nombre] = coords

                    # Marca las celdas como ocupadas en el tablero
                    for posicion_f, posicion_c in coords:
                        self.tablero[posicion_f, posicion_c] = CARACTER_BARCO
                        self.ocupadas.add((posicion_f, posicion_c))

                    # Termina los intentos del barco actual
                    break