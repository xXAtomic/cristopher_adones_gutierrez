class NodoHistorial:
    def __init__(self, paciente_id, fecha, registro):
        self.paciente_id = paciente_id
        self.fecha = fecha
        self.registro = registro
        self.izquierda = None
        self.derecha = None

class ArbolHistorial:
    def __init__(self):
        self.raiz = None

    def insertar(self, paciente_id, fecha, registro):
        self.raiz = self._insertar_recursivo(self.raiz, paciente_id, fecha, registro)

    def _insertar_recursivo(self, nodo, paciente_id, fecha, registro):
        if nodo is None:
            return NodoHistorial(paciente_id, fecha, registro)

        if fecha < nodo.fecha:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, paciente_id, fecha, registro)
        elif fecha > nodo.fecha:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, paciente_id, fecha, registro)
        else:
            # Si las fechas son iguales, puedes optar por agregar el nuevo registro a la derecha o izquierda, o incluso manejarlo como un error.
            nodo.derecha = self._insertar_recursivo(nodo.derecha, paciente_id, fecha, registro)

        return nodo

    def buscar(self, paciente_id, fecha):
        return self._buscar_recursivo(self.raiz, paciente_id, fecha)

    def _buscar_recursivo(self, nodo, paciente_id, fecha):
        if nodo is None:
            return None

        if paciente_id == nodo.paciente_id and fecha == nodo.fecha:
            return nodo.registro

        if fecha < nodo.fecha:
            return self._buscar_recursivo(nodo.izquierda, paciente_id, fecha)
        else:
            return self._buscar_recursivo(nodo.derecha, paciente_id, fecha)

    def buscar_por_paciente(self, paciente_id):
        registros = []
        self._buscar_por_paciente_recursivo(self.raiz, paciente_id, registros)
        return registros

    def _buscar_por_paciente_recursivo(self, nodo, paciente_id, registros):
        if nodo is not None:
            self._buscar_por_paciente_recursivo(nodo.izquierda, paciente_id, registros)
            if nodo.paciente_id == paciente_id:
                registros.append({"fecha": nodo.fecha, "registro": nodo.registro})
            self._buscar_por_paciente_recursivo(nodo.derecha, paciente_id, registros)

    def inorden(self):
      registros = []
      self._inorden_recursivo(self.raiz,registros)
      return registros

    def _inorden_recursivo(self, nodo, registros):
      if nodo is not None:
        self._inorden_recursivo(nodo.izquierda, registros)
        registros.append({"paciente_id":nodo.paciente_id, "fecha": nodo.fecha, "registro": nodo.registro})
        self._inorden_recursivo(nodo.derecha, registros)

# Crear un árbol de historial médico
arbol_historial = ArbolHistorial()

# Insertar registros médicos
arbol_historial.insertar(1, "2023-01-15", "Consulta general")
arbol_historial.insertar(2, "2023-02-20", "Examen de sangre")
arbol_historial.insertar(1, "2023-03-10", "Vacuna contra la gripe")
arbol_historial.insertar(2, "2023-04-05", "Radiografía de tórax")
arbol_historial.insertar(1, "2023-05-22", "Control de alergias")

# Buscar un registro específico
registro = arbol_historial.buscar(1, "2023-03-10")
print("Registro encontrado:", registro)

# Buscar todos los registros de un paciente
registros_paciente = arbol_historial.buscar_por_paciente(1)
print("Registros del paciente 1:", registros_paciente)

#Mostrar todos los registros ordenados por fecha
registros_ordenados = arbol_historial.inorden()
print("Registros ordenados por fecha:", registros_ordenados)