#implementacion del Arbol B(Insercion, busqueda, recorrido)
from proveedor import Proveedor

class NodoB:
    def __init__(self, orden):
        self.orden = orden              # Grado mínimo (orden del árbol B)
        self.claves = []               # Lista de claves (valores) almacenadas en este nodo
        self.hijos = []                # Lista de hijos de este nodo
        self.hoja = True               # Por defecto, todo nuevo nodo es una hoja

class ArbolB:
    def __init__(self, orden, key = lambda x: x.id):
        self.orden = orden             # Se define el orden del árbol (por ejemplo, 2)
        self.raiz = NodoB(orden)       # Se crea la raíz vacía inicialmente
        self.key = key                 # Función para comparar

    def insertar(self, proveedor: Proveedor):
        nodo_raiz = self.raiz

        # PASO 1: Verificamos si la raíz está llena (orden - 1 claves)
        if len(nodo_raiz.claves) == self.orden - 1:
            
            # Si está llena, se crea una nueva raíz
            nueva_raiz = NodoB(self.orden)
            nueva_raiz.hoja = False   # La nueva raíz no es hoja
            nueva_raiz.hijos.append(self.raiz)  # La raíz anterior se vuelve hijo

            # Se divide el hijo lleno (la raíz antigua)
            self.dividir(nueva_raiz, 0)

            # Ahora se inserta la clave en la nueva raíz
            self.insertar_en_nodo(nueva_raiz, proveedor)

            # Actualizamos la raíz del árbol
            self.raiz = nueva_raiz
        else:
            # Si la raíz no está llena, insertamos normalmente
            self.insertar_en_nodo(nodo_raiz, proveedor)

    def insertar_en_nodo(self, nodo_actual, proveedor):
        # PASO 2: Insertar la proveedor en el nodo correspondiente

        if nodo_actual.hoja:
            # Si el nodo actual es una hoja, simplemente insertamos la proveedor
            nodo_actual.claves.append(proveedor)
            nodo_actual.claves.sort(key = self.key)  # Ordenamos las claves (mantener orden)
        else:
            # Si no es hoja, buscamos en qué hijo debe ir la proveedor
            i = 0
            while i < len(nodo_actual.claves) and self.key(proveedor) > self.key(nodo_actual.claves[i]):
                i += 1

            # PASO 3: Verificamos si el hijo donde va la proveedor está lleno
            if len(nodo_actual.hijos[i].claves) == self.orden - 1:
                # Si está lleno, lo dividimos
                self.dividir(nodo_actual, i)

                # Luego de dividir, puede cambiar la posición donde debemos insertar
                if self.key(proveedor) > self.key(nodo_actual.claves[i]):
                    i += 1

            # PASO 4: Insertar recursivamente en el hijo adecuado
            self.insertar_en_nodo(nodo_actual.hijos[i], proveedor)

    def dividir(self, nodo_padre, i):
        orden = self.orden
        mitad = (orden - 1) // 2 # Es la mitad del número maximo de claves
        nodo_hijo = nodo_padre.hijos[i]

        # Se crea un nuevo nodo que será el hermano derecho del nodo dividido
        nuevo_nodo = NodoB(orden)
        nuevo_nodo.hoja = nodo_hijo.hoja  # El nuevo nodo será hoja si el hijo lo era

        # PASO 5: Se divide la lista de claves del hijo
        nuevo_nodo.claves = nodo_hijo.claves[mitad + 1:]     # Parte derecha
        proveedor_mitad = nodo_hijo.claves[mitad]        # proveedor del medio (va al padre)
        nodo_hijo.claves = nodo_hijo.claves[:mitad]  # Parte izquierda

        # PASO 6: Si el nodo no es hoja, también dividimos los hijos
        if not nodo_hijo.hoja:
            nuevo_nodo.hijos = nodo_hijo.hijos[mitad +1:]    # Hijos derechos
            nodo_hijo.hijos = nodo_hijo.hijos[:mitad +1]     # Hijos izquierdos

        # PASO 7: Insertamos la proveedor del medio en el padre
        nodo_padre.claves.insert(i, proveedor_mitad)

        # Insertamos el nuevo nodo como hijo del padre en la posición siguiente
        nodo_padre.hijos.insert(i + 1, nuevo_nodo)

    def mostrar(self, nodo_actual=None, nivel=0):
        if nodo_actual is None:
            nodo_actual = self.raiz

        # Convertir cada clave a string usando su __str__
        claves_str = [str(clave) for clave in nodo_actual.claves]
        print("  " * nivel + str(claves_str))

        for hijo in nodo_actual.hijos:
            self.mostrar(hijo, nivel + 1)


    def buscar(self, proveedor, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz

        # Buscar la posición donde la proveedor podría estar en este nodo
        i = 0
        while i < len(nodo_actual.claves) and self.key(proveedor) > self.key(nodo_actual.claves[i]):
            i += 1

        # Si la proveedor se encuentra en este nodo
        if i < len(nodo_actual.claves) and self.key(proveedor) == self.key(nodo_actual.claves[i]):
            print(f" proveedor {proveedor} encontrada en el nodo: {nodo_actual.claves}")
            return True

        # Si es hoja y no se encontró
        if nodo_actual.hoja:
            print(f" proveedor {proveedor} no encontrada.")
            return False

        # Si no es hoja, buscar recursivamente en el hijo correspondiente
        return self.buscar(proveedor, nodo_actual.hijos[i])

    # Método especifico para buscar por ID o servicio
    def busqueda(self, valor, nodo_actual=None, encontrados=None):
        if nodo_actual is None:
            nodo_actual = self.raiz
            encontrados = []

        # Buscar por ID
        if isinstance(valor, int):
            for p in nodo_actual.claves:
                if p.id == valor:
                    encontrados.append(p)

        # Buscar por servicio
        elif isinstance(valor, str):
            for p in nodo_actual.claves:
                if p.servicio.lower() == valor.lower():
                    encontrados.append(p)

        # Recorrer hijos
        for hijo in nodo_actual.hijos:
            self.busqueda(valor, hijo, encontrados)

        # Si es la llamada inicial, mostrar resultados
        if nodo_actual == self.raiz:
            if encontrados:
                for prov in encontrados:
                    print(f"Proveedor encontrado: {prov}")
            else:
                print(f"No se encontró ningún proveedor con '{valor}'")
            return encontrados
