from colorama import Fore

import Carrera_de_naipes
import Cuatro_en_raya
import Juego_del_gato
import Juego_del_ahorcado
import Batalla_naval

print(Fore.GREEN+ "██╗░░░██╗██╗██████╗░███████╗░█████╗░░░░░░██╗██╗░░░██╗███████╗░██████╗░░█████╗░░██████╗")
print(Fore.RED+   "██║░░░██║██║██╔══██╗██╔════╝██╔══██╗░░░░░██║██║░░░██║██╔════╝██╔════╝░██╔══██╗██╔════╝")
print(Fore.CYAN+  "╚██╗░██╔╝██║██║░░██║█████╗░░██║░░██║░░░░░██║██║░░░██║█████╗░░██║░░██╗░██║░░██║╚█████╗░   ")
print(Fore.YELLOW+"░╚████╔╝░██║██║░░██║██╔══╝░░██║░░██║██╗░░██║██║░░░██║██╔══╝░░██║░░╚██╗██║░░██║░╚═══██╗ ")
print(Fore.BLUE+  "░░╚██╔╝░░██║██████╔╝███████╗╚█████╔╝╚█████╔╝╚██████╔╝███████╗╚██████╔╝╚█████╔╝██████╔╝  ")
print(Fore.GREEN+ "░░░╚═╝░░░╚═╝╚═════╝░╚══════╝░╚════╝░░╚════╝░░╚═════╝░╚══════╝░╚═════╝░░╚════╝░╚═════╝░ ")
print(Fore.RED+   " ███████╗███╗░░██╗   ██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗  ")
print(Fore.CYAN+  " ██╔════╝████╗░██║   ██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║   ")
print(Fore.YELLOW+" █████╗░░██╔██╗██║   ██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║ ")
print(Fore.BLUE+  " ██╔══╝░░██║╚████║   ██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║   ")
print(Fore.GREEN+ " ███████╗██║░╚███║   ██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║                  ")
print(Fore.RED+   " ╚══════╝╚═╝░░╚══╝   ╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝                    ")
print(Fore.CYAN+  "                       ")



def menu_principal() -> int:
    """
    Función que muestra el menú principal para seleccionar cualquier programa
    :return: Entero válido para validar el dato
    """
    print(Fore.LIGHTYELLOW_EX+"** MENÚ PRINCIPAL ** ")
    print(Fore.CYAN+"1.- Carrera de naipes.")
    print(Fore.RED+"2.- Batalla naval ")
    print(Fore.MAGENTA+"3.- Juego del gato. ")
    print(Fore.BLUE+"4.- Juego de Cuatro en raya. ")
    print(Fore.CYAN+"5.- Juego del ahorcado.")
    print(Fore.RED+"6.- Salir. ")
    print(Fore.LIGHTBLUE_EX+" ")
    opcion = input("Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, 7):
        print("Opción no válida. Intenta de nuevo")
        opcion = input("Selecciona una opción: ")
    return int(opcion)





if __name__ == '__main__':
    opcion = 0
    while True:
        opcion = menu_principal()

        if opcion == 1:
            Carrera_de_naipes.jugar_carrera()
        elif opcion == 2:
            Batalla_naval.ejecutar_batalla_naval()
        elif opcion == 3:
            Juego_del_gato.ejecutar_juego_del_gato()
        elif opcion == 4:
            Cuatro_en_raya.ejecutar_cuatro_en_raya()
        elif opcion == 5:
            Juego_del_ahorcado.ejecutar_juego_ahorcado()
        elif opcion == 6:
            print("Saliendo, Gracias por jugar. :) ...")
            break
        else:
            print("Opción no válida. Ingresa un número del 1 al 6")
