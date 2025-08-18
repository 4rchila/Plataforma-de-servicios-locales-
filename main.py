from arbol_b import ArbolB
from proveedor import Proveedor
i = 0
continuar = True
Arbol_Proveedores = ArbolB(3)
while(continuar):
    print("Menu\n")
    print("1. Registrar Proveedor")
    print("2. Buscar Proveedores por servicio")
    print("3. Visualizar proveedores y  Servicios")
    print("4. buscar")
    print("5. Salir")

    opcion_Menu = int(input("Escribe el numero de la opcion que deseas ejecutar"))

    if opcion_Menu == 1:
        nombre = input("Escribe el nombre del Proveeor: ")
        servicio = input("Escribe el servicio que ofree el proveedor: ")
        calificacion = int(input("Escribe la calificacion promedio del proveedor: "))

        Proveedor.agregar_proveedor("",i+1, nombre, servicio,calificacion)
    elif opcion_Menu == 2:
        servicio = input("Escribe el servicio que deseas buscar")
        Arbol_Proveedores.busqueda(Arbol_Proveedores, servicio, None)
    elif opcion_Menu == 3:
        Arbol_Proveedores.recorrido_preorden()
    elif opcion_Menu == 4:
        key = int(input("escribe el Id de tu proveedro: "))
        Arbol_Proveedores.buscar(key)
    elif opcion_Menu == 5:
        continuar = False
    else:
        print("Opcion incorrecta. Vuelva a intentarlo")

