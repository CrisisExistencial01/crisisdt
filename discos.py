import os

# colores bonitos *brillitos*
verde = '\033[32m'
rojo = '\033[31m'
azul = '\033[34m'
celeste = '\033[36m'
amarillo = '\033[33m'
reset = '\033[0m'

def get_discos():
    return os.listdir('/run/media/cris/')

def list_discos():
    os.system('clear')
    l = get_discos()
    print()
    for i in range(0, len(l)):
        print(f"{verde}disco {i}: {l[i]}{reset}")

def get_devices():
    return os.system('ls /dev/ | grep sd')

def list_devices():
    os.system('clear')
    print()
    l = get_devices()
    print(l)

def devices_memory():
    os.system('clear')
    return os.system('df -h /dev/sd*')

def get_contenido(disco):
    os.system('clear')
    return os.listdir('/run/media/cris/' + disco)

def mostrar_contenido(disco):
    os.system('clear')
    l = get_contenido(disco)
    for i in range(0, len(l)):
        print(f"{celeste}archivo {i}: {l[i]}{reset}")

def menu_discos():
    print('1. Mostrar Discos')
    print('2. Mostrar Contenido')
    print('0. Salir')
    return int(input('Opción: '))

def handle_menu_discos():
    while True:
        print(f"{azul}Manejar Discos{reset}\n")

        opt = menu_discos()
        if opt == 1:
            list_discos()
        elif opt == 2:
            disco = int(input('Disco: '))
            l = get_discos()
            disco = l[disco]
            print(mostrar_contenido(disco))
        elif opt == 0:
            break
        else:
            print('Opción no válida')

def menu():
    print('1. Listar Discos')
    print('2. Listar Dispositivos')
    print('3. Memoria de dispositivos')
    print('4. Manejar Discos')
    print('0. Salir')
    return int(input('Opción: '))

def main():
    while True:
        opcion = menu()
        if opcion == 1:
            list_discos()
        elif opcion == 2:
            list_devices()
        elif opcion == 3:
            print(devices_memory())
        elif opcion == 4:
            print(f'{verde}Manejar Discos{reset}\n')
            opcion = menu_discos()
            handle_menu_discos()
        elif opcion == 0:
            break
        else:
            print('Opción no válida')
if __name__ == '__main__':
    main()
