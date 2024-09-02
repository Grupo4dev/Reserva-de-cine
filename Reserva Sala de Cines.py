import os
import pickle
import textwrap

def fnt_limpiarpantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def crear_sala_de_cine():
    print('Crear la sala del cine')
    try:
        filas = int(input('Filas: '))
        columnas = int(input('Columnas: '))
    except ValueError:
        print("Por favor, ingrese números válidos.")
        return []

    sala = []
    for i in range(filas):
        fila = [f"{chr(65 + i)}{j + 1}" for j in range(columnas)]
        sala.append(fila)
    
    return sala

def mostrar_sala(sala, reservados):
    if not sala:
        print("La sala aún no ha sido creada.")
        return
    
    print("\n" + "-" * 50)
    print("Estado actual de la sala de cine:")
    print("  " + " ".join([str(i + 1).rjust(2) for i in range(len(sala[0]))]))
    print("-" * 50 + "\n")
    
    for fila in sala:
        print(fila[0][0], end=" ")  # Letra de la fila (A, B, C, etc.)
        for asiento in fila:
            if asiento in reservados:
                print(" X", end=" ")  # Asiento reservado
            else:
                print(asiento.rjust(2), end=" ")  # Asiento disponible
        print()
    
    print("\n" + "-" * 50)

def reservar_asiento(sala, reservados):
    asiento = input("Ingrese el asiento que desea reservar (ej. A1): ").upper().strip()
    if not asiento:
        print("No se ingresó ningún asiento.")
        return
    nombre = input("Ingrese su nombre para la reservación: ").capitalize().strip()
    if not nombre:
        print("No se ingresó un nombre.")
        return
    
    for fila in sala:
        if asiento in fila:
            if asiento in reservados:
                print(f"El asiento {asiento} ya está reservado.")
            else:
                reservados[asiento] = nombre  
                print(f"Reserva exitosa. Asiento {asiento} reservado a nombre de {nombre}.")
            return
    print("El asiento no existe.")

def cargar_datos():
    try:
        with open("MiArchivo.dat", "rb") as archivo:
            return pickle.load(archivo)
    except FileNotFoundError:
        print("Archivo de datos no encontrado. No se han cargado reservas previas.")
        return {}
    except EOFError:
        print("El archivo de datos está vacío o corrupto.")
        return {}
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return {}

def guardar_datos(reservados):
    try:
        with open("MiArchivo.dat", "wb") as archivo:
            pickle.dump(reservados, archivo)
        print("Datos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def menu_sala_de_cine():
    fnt_limpiarpantalla()  # Limpiar pantalla antes de mostrar el menú
    print("\n" + "*" * 50)
    print("           *** Menú de la Sala de Cine ***")
    print("*" * 50 + "\n")
    
    opcs = [
        "1. Crear sala de cine",
        "2. Ver sala",
        "3. Reservar asiento",
        "4. Cargar sala",
        "5. Salir del programa"
    ]
    
    for opc in opcs:
        print(textwrap.fill(opc, width=50))
    
    print("\n" + "*" * 50)
    seleccion = input("Seleccione una opción: ")
    return seleccion

def main():
    sala = []
    reservados = cargar_datos()
    
    while True:
        fnt_limpiarpantalla()
        opcion = menu_sala_de_cine()
        
        if opcion == '1':
            fnt_limpiarpantalla()
            print("****** Creación de la sala ******")
            sala = crear_sala_de_cine()
            input("Presione <<Enter>> para continuar")
        elif opcion == '2':
            if not sala:
                fnt_limpiarpantalla()
                print("Primero debe crear la sala.")
            else:
                fnt_limpiarpantalla()
                mostrar_sala(sala, reservados)
            input("Presione <<Enter>> para continuar")
        elif opcion == '3':
            if not sala:
                fnt_limpiarpantalla()
                print("Primero debe crear la sala.")
            else:
                fnt_limpiarpantalla()
                reservar_asiento(sala, reservados)
            input("Presione <<Enter>> para continuar")
        elif opcion == '4':
            fnt_limpiarpantalla()
            reservados = cargar_datos()
            input("Presione <<Enter>> para continuar")
        elif opcion == '5':
            fnt_limpiarpantalla()
            guardar_datos(reservados)
            print("Gracias por usar el sistema de reservas.")
            break
        else:
            print("Opción no válida.")
            input("Presione <<Enter>> para continuar")
    
    print("\nAsientos reservados:")
    for asiento, nombre in reservados.items():
        print(f"Asiento {asiento} reservado a nombre de {nombre}.")

if __name__ == "__main__":
    main()
