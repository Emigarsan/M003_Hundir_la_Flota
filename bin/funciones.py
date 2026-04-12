# Método para que el jugador realice un disparo en el tablero del oponente

def realizar_disparo(disparo, tablero):
    acierto = False

    match tablero.tablero[disparo]:
        #Si el disparo acierta un barco, se marca con "X" y se indica que ha sido un acierto
        case "b":
            tablero.tablero[disparo] = "X"
            acierto = True
            print("¡Tocado!")
        #Si el disparo no acierta ningún barco, se marca con "-" y se indica que ha sido un fallo
        case " ":
            tablero.tablero[disparo] = "-"
            print("Agua.")
        #Si el disparo ya se ha realizado en esa posición, se indica que ya se ha disparado allí
        case "X", "-":
            print("Ya has disparado aquí.")
    
    # Se muestra el tablero del oponente después de cada disparo y devuelve si ha sido un acierto o no
    mostrar_tablero_oponente(tablero)
    return acierto

# Método para que la máquina realice un disparo aleatorio en el tablero del jugador

def realizar_disparo_aleatorio(tablero):
    acierto = False
    # La máquina genera coordenadas aleatorias para disparar
    disparo = (random.randint(0, DIMENSIONES_TABLERO - 1), random.randint(0, DIMENSIONES_TABLERO - 1))

    match tablero.tablero[disparo]:
        #Si el disparo acierta un barco, se marca con "X" y se indica que ha sido un acierto
        case "b":
            tablero.tablero[disparo] = "X"
            acierto = True
            print("¡Tocado!")
        #Si el disparo no acierta ningún barco, se marca con "-" y se indica que ha sido un fallo
        case " ":
            tablero.tablero[disparo] = "-"
            print("Agua.")
        #Si el disparo ya se ha realizado en esa posición, se indica que ya se ha disparado allí
        case "X", "-":
            print("Ya has disparado aquí.")

    mostrar_tablero(tablero)
    return acierto

# Se muestra el tablero del jugador con los barcos visibles

def mostrar_tablero(tablero):
    print(tablero.id_player)
    print(tablero.tablero)
    print("******************************************")

# Se muestra el tablero del oponente

def mostrar_tablero_oponente(tablero):
    # Se muestra el tablero del oponente con los barcos ocultos (reemplazando "b" por " ")
    tablero_oculto = np.where(tablero.tablero == "b", " ", tablero.tablero)
    print(tablero.id_player)
    print(tablero_oculto)
    print("******************************************")