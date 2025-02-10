


def mostrar_tablero(tablero: list) -> None:
    """
    Muestra el tablero del juego

    :param tablero: Lista como representacion del tablero
    """
    print("\n")
    for fila in tablero:
        print(" | ".join(fila)) #El .join es un método de cadena,  para formar una cadena a partir de subcadenas, en esta línea se ocupa para separar el | e intercalarlo
        print("-" * 8)




def verificar_ganador(tablero: list, jugador: str) -> bool:
    """
    Verifica si alguno de los jugadores ha ganado el juego

    :param tablero: el tablero que está representado en forma de lista
    :param jugador: Carácter que representa al jugador ('X' u 'O')
    :return: Valor booleano, True si el jugador ha ganado, False en caso contrario
    """
    
    for fila in tablero: #Verificando en todas las filas
        if all(casilla == jugador for casilla in fila): # all: devuelve True si todos los elementos de un iterable son verdaderos; de lo contrario, devuelve False
            return True


    for columna in range(3): #Verificando en todas las columnas
        if all(tablero[fila][columna] == jugador for fila in range(3)):
            return True
            
            
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)): #Verificando en todas las casillas
        return True
    return False


def tablero_lleno(tablero: list) -> bool:
    """
    Verifica si el tablero está lleno

    :param tablero: Lista del tablero
    :return: True si el tablero está lleno, False en caso contrario
    """
    return all(casilla != " " for fila in tablero for casilla in fila)


def movimiento_jugador(tablero: list, jugador: str) -> None:
    """
    Registra el movimiento de un jugador en el tablero.

    :param tablero: Listaque representa el tablero.
    :param jugador: Carácter que representa al jugador ('X' u 'O').
    """
    
    
    fila = validar_entrada("fila")
    columna = validar_entrada("columna")
    while tablero[fila][columna] != " ": #Mientras la "matriz" no sea un espacio vacio
        print("Esa casilla ya está ocupada. Intenta de nuevo:")
        fila = validar_entrada("fila")
        columna = validar_entrada("columna")
    tablero[fila][columna] = jugador




def validar_entrada(tipo: str) -> int:
    """
    Valida la entrada del usuario para filas o columnas.

    :param tipo: Tipo de entrada ("fila" o "columna").
    :return: Número entero entre 0 y 2.
    """
    
    
    entrada = input(f"Introduce el número de {tipo} (0, 1, 2): ")
    while not entrada.isnumeric() or int(entrada) not in [0, 1, 2]:
        print("Entrada inválida. Introduce un número válido")
        entrada = input(f"Introduce el número de {tipo} (0, 1, 2): ")
    return int(entrada)




def movimiento_cpu(tablero: list) -> None:
    """
    Realiza el movimiento de la CPU en cualquier casilla que esté desocupada

    :param tablero: Lista que representa el tablero
    """
    import random
    fila, columna = random.randint(0, 2), random.randint(0, 2)
    
    while tablero[fila][columna] != " ":
        fila, columna = random.randint(0, 2), random.randint(0, 2)
    tablero[fila][columna] = "🐷"


def jugar_contra_jugador() -> None:
    """
    Inicia una partida de juego del gato entre dos jugadores.
    """
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    mostrar_tablero(tablero)
    turno = "🐸"
    


    flag = 0
    while True:
        print(f"Turno de {turno}")
        movimiento_jugador(tablero, turno)
        mostrar_tablero(tablero)
        if verificar_ganador(tablero, turno):
            print(f"\n¡{turno} ha ganado!")
            break
        if tablero_lleno(tablero):
            print("\n¡Empate!")
            break
        turno = "🐷" if turno == "🐸" else "🐸"





def jugar_contra_cpu() -> None:
    """
    Inicia una partida de juego del gato entre un jugador y la CPU.
    """
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    mostrar_tablero(tablero)
    turno = "🐸"
    while True:
        if turno == "🐸":
            print("Tu turno:")
            movimiento_jugador(tablero, turno)
        else:
            print("Turno de la CPU:")
            movimiento_cpu(tablero)
        mostrar_tablero(tablero)
        if verificar_ganador(tablero, turno):
            print(f"{turno} ha ganado")
            break
        if tablero_lleno(tablero):
            print("Empate")
            break
        turno = "🐷" if turno == "🐸" else "🐸"







def menu() -> None:
    """
    Muestra el menú principal del juego del gato.
    """
    print("** MENÚ PRINCIPAL **")
    print("1. Jugar contra otro jugador")
    print("2. Jugar contra la CPU")
    print("3. Salir")




def iniciar_menu() -> int:
    """
    Inicia el menú y solicita una opción al usuario.

    :return: Opción seleccionada por el usuario.
    """
    opcion = input("Selecciona una opción: ")
    while opcion not in ["1", "2", "3"]:
        print("Opción inválida. Por favor, selecciona 1, 2 o 3.")
        opcion = input("Selecciona una opción: ")
    return int(opcion)





def ejecutar_juego_del_gato() -> None:
    flag = 0
    while True:
        menu()
        opcion = iniciar_menu()
        if opcion == 1:
            jugar_contra_jugador()
        elif opcion == 2:
            jugar_contra_cpu()
        elif opcion == 3:
            print("Saliendo...")
            break


if __name__ == '__main__':
    print(r"      _   _   _   _____    ____    ___      ____    _____   _          ____      _      _____    ___  ")
    print(r"     | | | | | | | ____|  / ___|  / _ \    |  _ \  | ____| | |        / ___|    / \    |_   _|  / _ \ ")
    print(r"  _  | | | | | | |  _|   | |  _  | | | |   | | | | |  _|   | |       | |  _    / _ \     | |   | | | |")
    print(r" | |_| | | |_| | | |___  | |_| | | |_| |   | |_| | | |___  | |___    | |_| |  / ___ \    | |   | |_| |")
    print(r"  \___/   \___/  |_____|  \____|  \___/    |____/  |_____| |_____|    \____| /_/   \_\   |_|    \___/ ")
    ejecutar_juego_del_gato()
