from arbol_b import ArbolB
from proveedor import Proveedor
import os

def obtener_calificacion():
    while True:
        try:
            calificacion = int(input("Escribe la calificación promedio del proveedor (número): "))
            if 1 <= calificacion <= 5:
                return calificacion
            else:
                print("Ingrese un valor entre 1 y 5.")
        except ValueError:
            print("Error: La calificación debe ser un número entero.")

continuar = True
arbol_proveedores = ArbolB(3)
contador_id = 0

print("--- INICIALIZANDO SISTEMA ---")
input("--- PRESIONE ENTER PARA CONTINUAR ---")
while continuar:
    os.system("cls")
    print("Gestionador de servicios.")
    print("1. Registrar proveedor de servicios.")
    print("2. Buscar proveedores por servicio")
    print("3. Listar trabajadores")
    print("4. Salir")

    try:
        opcion_menu = int(input("Escribe el número de la opción que deseas ejecutar: "))
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        input("Presiona Enter para continuar...")
        continue

    if opcion_menu == 1:
        nombre = input("Escribe el nombre del Proveedor: ").strip()
        servicio = input("Escribe el servicio que ofrece el proveedor: ").strip()

        if not nombre or not servicio:
            print("Error: El nombre y servicio no pueden estar vacíos.")
            input("Presiona Enter para continuar...")
            continue

        calificacion = obtener_calificacion()
        contador_id +=1
        nuevo_proveedor = Proveedor(contador_id , nombre, servicio, calificacion)
        arbol_proveedores.insertar(nuevo_proveedor)
        print("Proveedor agregado con éxito.")
        input("Presiona Enter para continuar...")

    elif opcion_menu == 2:
        os.system("cls")
        servicio = input("Escribe el servicio que deseas buscar: ").strip()
        if servicio:
            resultados = arbol_proveedores.buscar_por_servicio(servicio)
            if resultados:
                for proveedor in resultados:
                    print(f"Nombre: {proveedor.nombre}, Servicio: {proveedor.servicio}, Calificación: {proveedor.calificacion}")
            else:
                print("No se encontraron proveedores para ese servicio.")
        else:
            print("Error: El servicio no puede estar vacío.")
        input("Presiona Enter para continuar...")

    elif opcion_menu == 3:
        try:
            arbol_proveedores.listar_todos()
            input()
        except Exception as e:
            print(f"Error al recorrer el árbol: {e}")
        input("Presiona Enter para continuar...")

    elif opcion_menu == 4:
        print("Saliendo del sistema...")
        continuar = False
    else:
        print("Opción incorrecta. Vuelva a intentarlo.")
        input("Presiona Enter para continuar...")