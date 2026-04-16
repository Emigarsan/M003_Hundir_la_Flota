# **M003 Hundir la Flota**
### **¡Arrr pirata! Con este programa podrás sentirte como un verdadero capitán de los mares y enfrentarte en épicas batallas de hundir la flota⚓**
```
       |    |    |
      )_)  )_)  )_)
     )___))___))___)\
    )____)____)_____)\
  _____|____|____|____\__
  \                   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

## Contenido
---------------------------------------------------
- [Reglas del juego](#reglas-del-juego)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Uso](#uso)

## Reglas del juego
---------------------------------------------------
Este proyecto es un juego de “Hundir la flota”.

Al ejecutarlo:

- Se inicia el tablero del juego
- El jugador introduce coordenadas para atacar
- El programa indica si hay agua o impacto
- Gana quien hunda todos los barcos enemigos

## Estructura del proyecto
---------------------------------------------------
El proyecto está dividido en varios archivos:

- `variables.py` → contiene los datos iniciales del juego (tamaño de tablero, características de los barcos y codificación de disparos en el tablero).
- `funciones.py` → contiene las funciones de ataque y mostrar tablero.
- `clases.py` → define la clase tablero y los métodos de generar coordenadas y colocar los barcos.
- `main.py` → archivo principal que ejecuta el juego
- `requirements.txt` contiene las librerías necesarias para que el programa funcione correctamente.
## Uso
---------------------------------------------------
1. **Instalar las librerías pandas y numpy, si aún no las tienes instaladas**
   <details>
   <summary>Mostrar instrucciones</summary>

   ```bash
   pip install numpy
   pip install pandas
   ```

   </details>

⬇️

2. **Ejecutar el main.py**
   <details>
   <summary>Mostrar instrucciones</summary>

   ```bash
   python main.py
   ```

   </details>

⬇️

3. **¡Empieza el juego!**
  La dinámica de las partidas es:
  - Ambos jugadores (el usuario y la máquina), tendréis un tablero de posiciones de 10 x 10, donde los barcos se ubican de manera aleatoria.
  - Hay un total de 10 barcos: 4 barcos de 1 posición, 3 barcos de 2 posiciones, 2 barcos de 3 posiciones y 1 barco de 4 posiciones de eslora. ¡Tienes que hundirlos todos!
  - En cada ronda, cuando sea tu turno verás el tablero de la máquina arriba y el tuyo abajo, pero solo podrás ver tus barcos, marcados con una "O".
  - En tu turno, se te pedirá introducir un número de fila y un número de columna. **OJO: Las coordenadas tienen que estar siempre abarcadas entre el 0 y el 9 para que estén dentro del tablero**
  - Si aciertas, tendrás otro turno y en el tablero enemigo aparecerá una "X" donde hayas acertado. Si fallas, pierdes el turno y aparecerá una virgulilla ("~") para indicar la posición de agua.
  - Gana el que antes hunda todos los barcos del contrario.

⬇️

4. **Cheat mode**

Para comprobar que la máquina "no hace trampas", hay un modo testeo disponible. Con la variable:

```bash
OCULTO = False
```

podrás ver las posiciones de los barcos del enemigo.

---

```
       |    |    |
      )_)  )_)  )_)
     )___))___))___)\
    )____)____)_____)\
  _____|____|____|____\__
  \                   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

---

## ¡QUE GANE EL MEJOR! 🍀