"""Funciones auxiliares para la lógica de juego del Hundir la Flota.

Provee funcionalidades para:
- Generación de coordenadas aleatorias
- Ejecución de disparos y validación de impactos
- Visualización del tablero con opciones de ocultación
- Entrada de coordenadas del usuario con validación
- Comprobación del estado del juego
"""

import numpy as np
import random
import variables as var

def coordenadas_aleatorias(dim_tablero: int) -> tuple[int, int]:
    """Genera un par de coordenadas aleatorias válidas en el tablero.

    Args:
        dim_tablero (int): Dimensión del tablero (n x n).

    Returns:
        tuple[int, int]: Tupla (fila, columna) con valores entre 0 y dim_tablero-1.
    """
    # Selecciona fila aleatoria en el rango válido
    fila = random.randint(0, dim_tablero - 1)
    
    # Selecciona columna aleatoria en el rango válido
    columna = random.randint(0, dim_tablero - 1)
    
    return (fila, columna)

def realizar_disparo(tablero, disparo:tuple[int, int]=None) -> bool:
    """Ejecuta un disparo sobre un tablero y registra el resultado.

    Valida el impacto, actualiza el estado del tablero y notifica el resultado
    del disparo.

    Args:
        tablero: Instancia del tablero objetivo del disparo.
        disparo (tuple): Coordenadas del disparo (fila, columna).

    Returns:
        bool: True si el disparo impacta un barco (acierto), False en caso contrario.
    """
    acierto = False
    fila, columna = disparo

    print(f"\nDisparo en ({fila}, {columna})")

    # Evalúa el contenido de la celda y determina el resultado del disparo
    match tablero.tablero[disparo]:
        case var.CARACTER_BARCO:
            # Impacto exitoso: marca la celda como conquistada
            tablero.tablero[disparo] = var.CARACTER_IMPACTO
            acierto = True
            print("Resultado: ¡Tocado!")
        case var.CARACTER_AGUA:
            # Disparo en agua: marca como fallo
            tablero.tablero[disparo] = var.CARACTER_FALLO
            print("Resultado: Agua.")
        case var.CARACTER_IMPACTO, var.CARACTER_FALLO:
            # Celda ya visitada: no aplica cambio alguno
            print("Resultado: Casilla ya visitada.")
    
    return acierto

def mostrar_tablero(tablero, oculto:bool=False) -> None:
    """Renderiza el tablero en pantalla con formato de rejilla ordenada.

    Muestra números de fila y columna para facilitar la lectura del tablero.
    Opcionalmente oculta los barcos no impactados para modo oponente.

    Args:
        tablero: Instancia del tablero a visualizar.
        oculto (bool): Si es True, sustituye los barcos no impactados con espacios.
    """
    # Aplica máscara de privacidad si es necesario (modo oponente)
    if oculto:
        tablero_mostrar = np.where(tablero.tablero == var.CARACTER_BARCO, " ", tablero.tablero)
    else:
        tablero_mostrar = tablero.tablero

    dimension = tablero_mostrar.shape[0]
    ancho_celda = 3
    separador = "    +" + "+".join(["-" * ancho_celda] * dimension) + "+"
    cabecera = "     " + "  ".join(f"{col:>2}" for col in range(dimension))

    print("\n" + "=" * 60)
    print(f"TABLERO: {tablero.id_player}")
    print("=" * 60)
    print(cabecera)
    print(separador)

    for fila in range(dimension):
        celdas = []
        for col in range(dimension):
            valor = tablero_mostrar[fila, col]
            celdas.append(f" {valor} ")
        print(f" {fila:>2} |" + "|".join(celdas) + "|")
        print(separador)

    if oculto:
        print(f"\nLeyenda: '{var.CARACTER_IMPACTO}'= Impacto  '{var.CARACTER_FALLO}'= Fallo  '{var.CARACTER_AGUA}'= Desconocido")
    else:
        print(f"\nLeyenda: '{var.CARACTER_BARCO}'= Barco  '{var.CARACTER_IMPACTO}'= Impacto  '{var.CARACTER_FALLO}'= Fallo  '{var.CARACTER_AGUA}'= Agua")

    print("=" * 60)

# Solicita coordenadas válidas del jugador con validación de entrada
def pedir_coordenadas() -> tuple[int, int]:
    """Solicita al jugador que ingrese coordenadas válidas con validación.

    Valida que:
    - Los valores ingresados sean de tipo entero.
    - Las coordenadas estén dentro del rango [0, DIMENSIONES_TABLERO).

    Returns:
        tuple[int, int]: Coordenadas validadas (fila, columna).
    """
    while True:
        try:
            # Solicita entrada de la fila
            fila = int(input(f"Fila (0-{var.DIMENSIONES_TABLERO - 1}): "))
            # Solicita entrada de la columna
            columna = int(input(f"Columna (0-{var.DIMENSIONES_TABLERO - 1}): "))
            
            # Valida que ambas coordenadas estén dentro del rango válido
            if 0 <= fila < var.DIMENSIONES_TABLERO and 0 <= columna < var.DIMENSIONES_TABLERO:
                return (fila, columna)
            # Notifica si las coordenadas están fuera de rango
            print("Coordenadas fuera de rango. Intenta de nuevo.")
        except ValueError:
            # Gestiona entrada no numérica
            print("Introduce un numero valido.")

# Valida si una casilla ya fue impactada en disparos anteriores

def casilla_ya_disparada(tab, disparo: tuple[int, int]) -> bool:
    """Verifica si una casilla ya ha sido objetivo de un disparo previo.

    Args:
        tab: Instancia del tablero a consultar.
        disparo (tuple): Coordenadas a verificar (fila, columna).

    Returns:
        bool: True si la casilla fue impactada (X) o marcada como fallo (-),
              False si aún no ha sido objeto de disparo alguno.
    """
    return tab.tablero[disparo] in (var.CARACTER_IMPACTO, var.CARACTER_FALLO)

# Evalúa el estado del juego: verifica si quedan barcos sin hundir

def comprobar_fin(tab) -> bool:
    """Comprueba si todos los barcos han sido hundidos (fin de partida).

    Itera el tablero completo para detectar si aún existe alguna casilla
    que represente un barco sin impactar. Un barco se considera hundido
    cuando todas sus celdas son impacto (X) o no quedan barcos visibles.

    Args:
        tab: Instancia del tablero a evaluar.

    Returns:
        bool: True si no quedan barcos sin hundir (fin de partida),
              False si aún hay barcos activos.
    """
    # Itera cada fila del tablero
    for fila in tab.tablero:
        # Itera cada casilla de la fila
        for casilla in fila:
            # Detecta si existe una casilla que NO sea agua, impacto ni fallo
            # (es decir, una casilla de barco que no ha sido impactada)
            if casilla not in (var.CARACTER_AGUA, var.CARACTER_IMPACTO, var.CARACTER_FALLO):
                # Aún quedan barcos vivos
                return False
    # No se encontraron barcos vivos: partida terminada
    return True