from proveedor import Proveedor

class NodoB:
    def __init__(self, orden):
        self.orden = orden
        self.claves = []
        self.hijos = []
        self.hoja = True

class ArbolB:
    def __init__(self, orden, key=lambda x: x.id):
        self.orden = orden
        self.raiz = NodoB(orden)
        self.key = key

    def insertar(self, proveedor: Proveedor):
        if len(self.raiz.claves) == 2 * self.orden - 1:
            nueva_raiz = NodoB(self.orden)
            nueva_raiz.hoja = False
            nueva_raiz.hijos.append(self.raiz)
            self.dividir(nueva_raiz, 0)
            self.raiz = nueva_raiz
        self._insertar_no_lleno(self.raiz, proveedor)

    def _insertar_no_lleno(self, nodo, proveedor):
        i = len(nodo.claves) - 1
        
        if nodo.hoja:
            while i >= 0 and self.key(proveedor) < self.key(nodo.claves[i]):
                i -= 1
            nodo.claves.insert(i + 1, proveedor)
        else:
            while i >= 0 and self.key(proveedor) < self.key(nodo.claves[i]):
                i -= 1
            i += 1
            
            if len(nodo.hijos[i].claves) == 2 * self.orden - 1:
                self.dividir(nodo, i)
                if self.key(proveedor) > self.key(nodo.claves[i]):
                    i += 1
            self._insertar_no_lleno(nodo.hijos[i], proveedor)

    def dividir(self, padre, indice):
        orden = self.orden
        hijo = padre.hijos[indice]
        nuevo_nodo = NodoB(orden)
        nuevo_nodo.hoja = hijo.hoja
        
        clave_medio = hijo.claves[orden - 1]
        
        nuevo_nodo.claves = hijo.claves[orden:]
        hijo.claves = hijo.claves[:orden - 1]
        
        if not hijo.hoja:
            nuevo_nodo.hijos = hijo.hijos[orden:]
            hijo.hijos = hijo.hijos[:orden]
        
        padre.claves.insert(indice, clave_medio)
        padre.hijos.insert(indice + 1, nuevo_nodo)

    def buscar_por_id(self, id_buscar, nodo=None):
        if nodo is None:
            nodo = self.raiz
        
        i = 0
        while i < len(nodo.claves) and id_buscar > self.key(nodo.claves[i]):
            i += 1
        
        if i < len(nodo.claves) and id_buscar == self.key(nodo.claves[i]):
            return nodo.claves[i]  
        
        if nodo.hoja:
            return None  
        
        return self.buscar_por_id(id_buscar, nodo.hijos[i])

    def buscar_por_servicio(self, servicio_buscar, nodo=None, resultados=None):
        """Búsqueda por servicio (requiere recorrido completo)"""
        if nodo is None:
            nodo = self.raiz
            resultados = []
        
        for proveedor in nodo.claves:
            if proveedor.servicio.lower() == servicio_buscar.lower():
                resultados.append(proveedor)
        
        if not nodo.hoja:
            for hijo in nodo.hijos:
                self.buscar_por_servicio(servicio_buscar, hijo, resultados)
        
        return resultados

    def recorrido_inorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        
        resultados = []
        
        for i in range(len(nodo.claves)):
            if not nodo.hoja:
                resultados.extend(self.recorrido_inorden(nodo.hijos[i]))
            resultados.append(nodo.claves[i])
        
        if not nodo.hoja:
            resultados.extend(self.recorrido_inorden(nodo.hijos[-1]))
        
        return resultados

    def mostrar_arbol(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz
        
        print("  " * nivel + f"Nivel {nivel}: ", end="")
        print([f"ID:{p.id}" for p in nodo.claves])
        
        for hijo in nodo.hijos:
            self.mostrar_arbol(hijo, nivel + 1)

    def listar_todos(self):
        proveedores = self.recorrido_inorden()
        for proveedor in proveedores:
            print(proveedor)
        return proveedores