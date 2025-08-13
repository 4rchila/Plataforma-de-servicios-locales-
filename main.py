#Archivo de punto de entrada del programa (menu principal y flujo general)

# Prueba de los metodos del árbol B
import arbol_b
from proveedor import Proveedor
def main():
    arbol = arbol_b.ArbolB(orden=3) #Claves maximas 2
    #Insertar claves

    proveedor1 = Proveedor(1, "Proveedor A", "Servicio A", 4.5)
    proveedor2 = Proveedor(2, "Proveedor B", "Servicio B", 3.8)
    proveedor3 = Proveedor(3, "Proveedor C", "Servicio C", 4.0) 
    proveedor4 = Proveedor(4, "Proveedor D", "Servicio D", 5.0)
    proveedor5 = Proveedor(5, "Proveedor E", "Servicio E", 2.5)
    proveedor6 = Proveedor(6, "Proveedor F", "Servicio F", 3.0)
    proveedor7 = Proveedor(7, "Proveedor G", "Servicio G", 4.2)

    arbol.insertar(proveedor1)
    print(f"Clave insertada: {proveedor1.id} - {proveedor1.nombre}")
    arbol.insertar(proveedor2)
    print(f"Clave insertada: {proveedor2.id} - {proveedor2.nombre}")
    arbol.insertar(proveedor3)
    print(f"Clave insertada: {proveedor3.id} - {proveedor3.nombre}")
    arbol.insertar(proveedor4)
    print(f"Clave insertada: {proveedor4.id} - {proveedor4.nombre}")
    arbol.insertar(proveedor5)
    print(f"Clave insertada: {proveedor5.id} - {proveedor5.nombre}")
    arbol.insertar(proveedor6)
    print(f"Clave insertada: {proveedor6.id} - {proveedor6.nombre}")
    arbol.insertar(proveedor7)
    print(f"Clave insertada: {proveedor7.id} - {proveedor7.nombre}")
    arbol.mostrar()

    # Buscar claves
    print("Buscando proveedores...")
    arbol.busqueda(1)
    arbol.busqueda(6)
    arbol.busqueda("Servicio A")
    arbol.busqueda("fadsjdls")
    print("-" * 30)
    

main()