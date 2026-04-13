from variables import DIMENSIONES_TABLERO, BARCOS, NOMBRES_JUGADORES, CARACTER_IMPACTO, CARACTER_FALLO
from classes import tablero
from funciones import realizar_disparo, realizar_disparo_aleatorio, mostrar_tablero, mostrar_tablero_oponente


# FUNCIONES AUXILIARES - TODO pasar a funciones.py o meter en los métodos 

# Para pedir el input al jugador y validar que esta dentro de rango 0-TABLERO y sea tipo int
def pedir_coordenadas():

    while True:
        try:
            fila = int(input(f"Fila (0-{DIMENSIONES_TABLERO - 1}): "))
            columna = int(input(f"Columna (0-{DIMENSIONES_TABLERO - 1}): "))
            if 0 <= fila < DIMENSIONES_TABLERO and 0 <= columna < DIMENSIONES_TABLERO:
                return (fila, columna)
            print("Coordenadas fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Introduce un numero valido.")

# Comprueba que se no haya disparado ya a esa celda. TODO Meter dentro de las funciones de disparo en vez de funcion suelta?

def casilla_ya_disparada(tab, disparo):
    return tab.tablero[disparo] in (CARACTER_IMPACTO, CARACTER_FALLO)

# Recorre tablero para comprobar si queda algun barco vivo 
# barco vivo = casilla no es agua (" "), impacto ("X") ni fallo ("-")

def comprobar_fin(tab):
    for fila in tab.tablero:
        for casilla in fila:
            if casilla not in (" ", CARACTER_IMPACTO, CARACTER_FALLO):
                return False
    return True


# ============================================================
# HUNDIR LA FLOTA --- BUCLE PRINCIPAL
# ============================================================

def main():
    # Mensaje de bienvenida - SI HAY TIEMPO añadir mas f-string?
    print("=" * 50)
    print("   BIENVENIDO A HUNDIR LA FLOTA")
    print("=" * 50)
    print("\nReglas:")
    print(f"- Tablero de {DIMENSIONES_TABLERO}x{DIMENSIONES_TABLERO}")
    print("- Barcos: 1x4, 2x3, 3x2, 4x1")
    print("- Si tocas, repites turno")
    print("- Gana quien hunda todos los barcos del rival\n")

    # Iniciar tableros para jugador y maquina, empieza siempre el jugador
    tablero_jugador = tablero(BARCOS, NOMBRES_JUGADORES[0])
    tablero_maquina = tablero(BARCOS, NOMBRES_JUGADORES[1])

    tablero_jugador.colocar_barcos()
    tablero_maquina.colocar_barcos()

    turno_jugador = True

    # Bucle de juego - al jugador le imprime un mensaje y pide el input, lo valida, y repite el el turno mientras realizar_disparo devuelva True
    #                   la maquina simplemente dispara aleatoriamente mientras sea su turno
    while True:

        # ---- TURNO DEL JUGADOR ----
        if turno_jugador:
            print("\n>>> TURNO DEL JUGADOR <<<")
            mostrar_tablero(tablero_jugador)
            mostrar_tablero_oponente(tablero_maquina)
            # pedir_coordenadas deberia llamarse desde funciones.py 
            disparo = pedir_coordenadas()

            # Validar que el disparo no sea repe
            if casilla_ya_disparada(tablero_maquina, disparo):
                print("Ya has disparado en esa casilla. Elige otra.")
                continue
            # Realiza el disparo
            tocado = realizar_disparo(disparo, tablero_maquina)
            # comprobar_fin deberia estar en funciones.py
            if comprobar_fin(tablero_maquina):
                print("\nHas hundido toda la flota enemiga!")
                print("VICTORIA DEL JUGADOR!")
                break
            # Si tocado es True, repite turno. De lo contrario, acaba.
            if tocado:
                print("Repites turno.")
            else:
                turno_jugador = False

        # ---- TURNO DE LA MAQUINA ----
        else:
            print("\n>>> TURNO DE LA MAQUINA <<<")
            # TODO Ahora mismo la maquina no sabe que no debe no repetir disparos 
            tocado = realizar_disparo_aleatorio(tablero_jugador)
            # comprobar_fin deberia estar en funciones.py
            if comprobar_fin(tablero_jugador):
                print("\nLa maquina ha hundido toda tu flota...")
                print("DERROTA.")
                break
            # Si tocado es True, repite turno. De lo contrario, acaba.
            if tocado:
                print("La maquina repite turno.")
            else:
                turno_jugador = True

    # Mensaje de fin de partida
    print("\n--- TABLERO FINAL ---")
    mostrar_tablero(tablero_jugador)
    mostrar_tablero(tablero_maquina)
    print("\nGracias por jugar a Hundir la Flota!")


if __name__ == "__main__":
    main()
