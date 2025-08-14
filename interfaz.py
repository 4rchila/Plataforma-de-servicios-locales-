import os

detenerse = False

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

    elif opcion == 2:
        os.system("cls")
        print("Buscar proveedores de servicios.")

    elif opcion == 3:
        os.system("cls")
        print("Listar trabajadores.")

    elif opcion == 4:
        os.system("cls")
        print("--- CERRANDO SISTEMA ---")
        detenerse = True
    
    else:
        print("Ingrese una opción válida.")