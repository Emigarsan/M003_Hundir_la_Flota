# Dimensiones del tablero de juego (10x10)
DIMENSIONES_TABLERO = 10

# Caracteres para representar diferentes estados en el tablero
CARACTER_AGUA = " "        # Casilla sin explorar o sin barco
CARACTER_BARCO = "O"       # Casilla con un barco
CARACTER_IMPACTO = "X"     # Casilla donde se acertó un barco
CARACTER_FALLO = "-"       # Casilla donde se falló (agua)

# Nombres de los jugadores
NOMBRES_JUGADORES = ["Jugador 1", "Maquina"]

# Variable de control para saber de quién es el turno
TU_TURNO = True
# Variable para ocultar o mostrar los barcos del oponente (True = oculto, False = visible) - se puede usar para testeo
OCULTO = False


# Diccionario que almacenará información de los barcos
BARCOS = {}

# Bucle para generar dinámicamente los barcos
# barco: tamaño del barco (1 a 4 celdas)
# indice: número secuencial de barcos del mismo tamaño
for barco in range(1, 5):
    # Para cada tamaño, se crean (5-tamaño) barcos
    # Barcos de tamaño 1: 4 barcos
    # Barcos de tamaño 2: 3 barcos
    # Barcos de tamaño 3: 2 barcos
    # Barcos de tamaño 4: 1 barco
    for indice in range(5 - barco):
        # Crea un nombre único para cada barco (ej: "barco1_1", "barco2_1")
        nombre_barco = f"barco{barco}_{indice + 1}"
        # Asigna el tamaño del barco al diccionario
        BARCOS[nombre_barco] = barco