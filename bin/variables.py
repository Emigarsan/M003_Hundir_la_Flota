"""Constantes y configuración global para el juego Hundir la Flota.

Define parámetros del tablero, símbolos de representación, nombres de jugadores
y variables de estado del juego.
"""

# Dimensión estándar del tablero de juego: 10 filas x 10 columnas
DIMENSIONES_TABLERO = 10

# Símbolos de representación para distintos estados de las casillas del tablero
CARACTER_AGUA = " "        # Estado inicial: casilla sin explorar, sin barco
CARACTER_BARCO = "O"       # Posición de un barco sin impacto
CARACTER_IMPACTO = "X"     # Impacto exitoso contra un barco
CARACTER_FALLO = "-"       # Disparo fallido (agua)

# Identificadores de los dos jugadores del juego
NOMBRES_JUGADORES = ["Jugador 1", "Maquina"]

# Bandera de control de turno: True indica turno del jugador, False indica turno de la máquina
TU_TURNO = True

# Bandera de visibilidad: True oculta barcos del oponente, False los muestra (para debug y testeo controlado)
OCULTO = False

# Diccionario que almacena la configuración de barcos: nombre -> eslora (longitud)
BARCOS = {}

# Inicialización dinámica de la flota según configuración estándar.
# Estructura: 4 barcos de eslora 1, 3 de eslora 2, 2 de eslora 3, 1 de eslora 4
for eslora in range(1, 5):
    # Cantidad de barcos de esta eslora = (5 - eslora)
    # Ejemplo: eslora=1 → 4 barcos; eslora=4 → 1 barco
    cantidad_barcos = 5 - eslora
    
    for indice in range(cantidad_barcos):
        # Genera identificador único: "barco<eslora>_<número_secuencial>"
        # Ejemplo: "barco1_1", "barco1_2", "barco2_1", etc.
        nombre_barco = f"barco{eslora}_{indice + 1}"
        BARCOS[nombre_barco] = eslora