from arbol_b import ArbolB
from proveedor import Proveedor
import os

i = 0
continuar = True
Arbol_Proveedores = ArbolB(3)

while continuar:
    os.system("cls")
    print("\n--- Menú ---")
    print("Ingrese la opción que desee realizar.")
    print("1. Registrar proveedor de servicios.")
    print("2. Buscar proveedores por servicio")
    print("3. Listar trabajadores")
    print("4. Salir")

    try:
        opcion_Menu = int(input("Escribe el número de la opción que deseas ejecutar: "))
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        continue

    if opcion_Menu == 1:
        try:
            nombre = input("Escribe el nombre del Proveedor: ").strip()
            servicio = input("Escribe el servicio que ofrece el proveedor: ").strip()
            calificacion = int(input("Escribe la calificación promedio del proveedor (número): "))
            while calificacion < 1 or calificacion > 5:
                print("Ingrese un valor adecuado.")
                calificacion = int(input("Calificación: "))
            
            # Validación básica
            if not nombre or not servicio:
                print("Error: El nombre y servicio no pueden estar vacíos.")
                continue

            Proveedor.agregar_proveedor("", i + 1, nombre, servicio, calificacion)
            print("Proveedor agregado con éxito.")
            i += 1
        except ValueError:
            print("Error: La calificación debe ser un número entero.")

    elif opcion_Menu == 2:
        os.system("cls")
        servicio = input("Escribe el servicio que deseas buscar: ").strip()
        if servicio:
            Arbol_Proveedores.busqueda(Arbol_Proveedores, servicio, None)
        else:
            print("Error: El servicio no puede estar vacío.")

    elif opcion_Menu == 3:
        try:
            Arbol_Proveedores.recorrido_preorden()
        except Exception as e:
            print(f"Error al recorrer el árbol: {e}")

    # elif opcion_Menu == 4:
        # try:
            # key = int(input("Escribe el Id del proveedor: "))
            # Arbol_Proveedores.buscar(key)
        # except ValueError:
            # print("Error: El Id debe ser un número.")
            
    elif opcion_Menu == 4:
        print("Saliendo del sistema...")
        continuar = False
    else:
        print("Opción incorrecta. Vuelva a intentarlo.")