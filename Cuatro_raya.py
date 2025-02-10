# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Descripción:
# Juego cuatro en raya con dos modos de juego: J vs J y J vs CPU.

from colorama import Fore
# ///////////////////////////////////////////////////////////////////////////////////////// Menu Jugabilidad.
def menu_jugabilidad():
    """

    :return: retorna un valor entero según haya elegido el usuario.
    """
    print(Fore.BLUE +"*** Modo de juego ***")
    print(Fore.BLUE + "[1].- Jugador contra jugador")
    print(Fore.BLUE + "[2].- Jugador con CPU")
    print(Fore.BLUE + "[3].- Salir")
    opcion = input(Fore.BLUE +  "Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, 4):
        print(Fore.BLUE + "Opción no válida. Intenta de nuevo")
        opcion = input(Fore.BLUE + "Selecciona una opción: ")
    return int(opcion)
# ///////////////////////////////////////////////////////////////////////////////////////// Función para limpiar la pantalla.
def limpiar() -> None:
    """
    Imprime varias lineas en blanco, para simular una pantalla limpia.
    """
    print("\n" * 50)

# ///////////////////////////////////////////////////////////////////////////////////////// Función crear y mostrar el tablero.
def crear_tablero() -> list:
    """
    Crea un tablero vacío de 6 filas por 7 columnas.
    :return: Regresa el tablero en forma de lista.
    """
    return [[" " for _ in range(7)] for _ in range(6)]

def mostrar_tablero(tablero) -> None:
    """
    Muestra el tablero en pantalla.
    :param:recibe el tablero vacio o con las fichas existentes, y posteriormente lo imprime en pantalla
    """
    print(" 1    2    3    4    5    6    7")
    print("---------------------------------")
    for fila in tablero:
        print("|" + "|".join(f" {celda} " for celda in fila) + "|")
        print("---------------------------------")
# ///////////////////////////////////////////////////////////////////////////////////////// Función para colocar fichas.
def colocar_ficha(tablero, columna, ficha) -> bool:
    """
    Coloca una ficha en la columna indicada si es posible.
    :param tablero: Recibe el tablero con las fichas existentes.
    :param columna: Recibe la columna elejida por el usuario.
    :param ficha: Recibe X o O, según el turno.
    :return: Regresa un valor booleano, una vez validado si hay lugar disponible en la columna elejida.
    """

    for fila in reversed(tablero): # Reversed se utiliza para rocesar elementos en orden inverso, en este caso lo uso para recorrer el contenido al revés y rellenar el espacio vacio al fondo de la columna.
        if fila[columna] == " ":
            fila[columna] = ficha
            return True
    return False
# ///////////////////////////////////////////////////////////////////////////////////////// Función para buscar ganador.
def verificar_victoria(tablero, ficha) -> bool:
    """
    Verifica si hay cuatro en raya para la ficha dada.
    :param tablero: Recibe el tablero con las fichas existentes.
    :param ficha: Reciba la ficha que se acaba de colocar.
    :return: Regresa un valor booleano, una vez verificando si no existe un cuatro en raya de la ficha que se acaba de colocar.
    """


    for fila in tablero:        # ................................ Verificar filas.
        for col in range(4):
            if all(fila[col + i] == ficha for i in range(4)):
                return True


    for col in range(7):        # ................................ Verificar columnas.
        for fila in range(3):
            if all(tablero[fila + i][col] == ficha for i in range(4)):
                return True


    for fila in range(3):       # ................................ Verificar diagonales hacia abajo.
        for col in range(4):
            if all(tablero[fila + i][col + i] == ficha for i in range(4)):
                return True


    for fila in range(3, 6):    # ................................ Verificar diagonales hacia arriba.
        for col in range(4):
            if all(tablero[fila - i][col + i] == ficha for i in range(4)):
                return True

    return False
# ///////////////////////////////////////////////////////////////////////////////////////// Función jugador vs jugador.
def jugar_vs_jugador() -> None:
    """
    Modo de juego: Jugador contra Jugador.
    :return:
    """

    tablero = crear_tablero()
    turno = 0
    fichas = ["X", "O"]

    while True:
        limpiar()
        mostrar_tablero(tablero)
        ficha_actual = fichas[turno % 2]        # ................................ Se va intercalando la ficha.
        print(f"Turno del jugador {turno % 2 + 1} ({ficha_actual})")

        columna = 1
        while columna < 0 or columna >= 7:
            entrada = input("Elige una columna (1-7): ")
            if entrada.isdigit():               # ................................ .isdigit varifica que el dato ingresado es un número.
                columna = int(entrada) - 1
                if columna < 0 or columna >= 7:
                    print("La columna no existe. Intenta de nuevo.")
            else:
                print("Entrada inválida. Por favor, ingresa un número entre 1 y 7.")

        if not colocar_ficha(tablero, columna, ficha_actual):   # ................................ .Verifica que la columna tiene espacio de lo contrario pide otra columna .
            print("Columna llena. Intenta otra vez.")
            continue

        if verificar_victoria(tablero, ficha_actual):
            mostrar_tablero(tablero)
            print(f"¡Jugador {turno % 2 + 1} ({ficha_actual}) gana!")
            break

        if all(tablero[0][col] != " " for col in range(7)):
            mostrar_tablero(tablero)
            print("¡El juego termina en empate!")
            break

        turno += 1
# ///////////////////////////////////////////////////////////////////////////////////////// Función jugador vs cpu.
def jugar_vs_cpu() -> None:
    """
    Modo de juego: Jugador contra CPU.
    """
    import random
    tablero = crear_tablero()
    turno = 0
    fichas = ["X", "O"]

    while True:
        limpiar()
        mostrar_tablero(tablero)
        ficha_actual = fichas[turno % 2]
        if turno % 2 == 0:      # ................................ Si el módulo es igual a cero es turno del usuario.
            print(f"Turno del jugador (X)")
            columna = -1
            while columna < 0 or columna >= 7:
                entrada = input("Elige una columna (1-7): ")
                if entrada.isdigit():       # .isdigit verifica si el dato ingresado es un número
                    columna = int(entrada) - 1
                    if columna < 0 or columna >= 7:
                        print("La columna no existe. Intenta de nuevo.")
                else:
                    print("Entrada inválida. Por favor, ingresa un número entre 1 y 7.")

            if not colocar_ficha(tablero, columna, ficha_actual):
                print("Columna llena. Intenta otra vez.")
                continue
        else:                   # ................................ Turno de la CPU.
            print("Turno de la CPU (O)")
            columna = random.randint(1,7)
            colocar_ficha(tablero, columna, ficha_actual)

        if verificar_victoria(tablero, ficha_actual):   # ................................ Verificación para saber si hay un ganador.
            limpiar()
            mostrar_tablero(tablero)
            if turno % 2 == 0:
                print(f"Jugador (X) gana!")
            else:
                print("La CPU (O) gana!")
            break

        if all(tablero[0][col] != " " for col in range(7)):     # ................................ Cunado el tablero este lleno y no haya ganador.
            mostrar_tablero(tablero)
            print("El juego termina en empate!")
            break

        turno += 1
# ///////////////////////////////////////////////////////////////////////////////////////// Función main.
def ejecutar_cuatro_en_raya() -> None:
    """
    Función donde se encuentra las llamdas a funciones principales..
    :return:
    """
    opcion = menu_jugabilidad()
    if opcion == 1:
        jugar_vs_jugador()
    else:
       jugar_vs_cpu()

# ///////////////////////////////////////////////////////////////////////////////////////// Codigo a nivel de modulo.
if __name__ == '__main__':
    ejecutar_cuatro_en_raya()