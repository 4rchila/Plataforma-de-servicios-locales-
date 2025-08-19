import os

detenerse = False
idTrabajador = 1

os.system("cls")
print("--- INICIANDO SISTEMA ---")
input("--- PRESIONE CUALQUIER TECLA PARA INICIAR ---")

while detenerse == False:
    os.system("cls")
    print("--- REGISTRADOR DE TRABAJADORES INDEPENDIENTES ---")
    print("Ingrese la opción que desee realizar.")
    print("1. Registrar proveedores de servicios.")
    print("2. Buscar proveedores de servicios.")
    print("3. Listar trabajadores.")
    print("4. Salir.")
    opcion = int(input("Opción: "))

    if opcion == 1:
        os.system("cls")
        print("Registrar proveedores de servicios.")
        print("Ingrese los datos solicitados a continuación para registrar un nuevo trabajador.")
        nombre = input("Nombres y apellidos: ")
        servicio = input("Servicio o profesión: ")
        print("Ingrese la calificación de 1 a 5 estrellas.")
        estrellas = int(input("Calificación: "))
        while estrellas < 1 or estrellas > 5:
            print("Ingrese un valor adecuado.")
            estrellas = int(input("Calificación: "))
        id = idTrabajador
        idTrabajador += 1            

    elif opcion == 2:
        os.system("cls")
        print("Buscar proveedores de servicios.")
        print("Ingrese la opción que desee.")
        print("1. Buscar por nombre.")
        print("2. Buscar por calificación.")
        opcionBuscador = int(input("Opción: "))

        if opcionBuscador == 1:
            print("Ingrese el nombre del trabajador")
            nombreBuscador = input("Nombre: ")

        elif opcionBuscador == 2:
            print("Ingrese la calificación que deseea filtrar.")
            calificacionBuscador = int(input("Calificación: "))

        else:
            print("Ingrese una opción válida.")

    elif opcion == 3:
        os.system("cls")
        print("Listar trabajadores.")
        print("Estos son los trabajadores existentes: ")

    elif opcion == 4:
        os.system("cls")
        print("--- CERRANDO SISTEMA ---")
        detenerse = True
    
    else:
        print("Ingrese una opción válida.")