"""
======================================================================
           RESUMEN: ESTRUCTURA DE DATOS - PILA (STACK)
======================================================================

1. DEFINICIÓN Y CONCEPTOS FUNDAMENTALES
   Una Pila (Stack) es un tipo de dato abstracto que organiza la
   información de manera lineal. Se rige por el principio LIFO
   (Last-In-First-Out), lo que significa que el último elemento
   en entrar es el primero en salir.

   Operaciones Principales:
   - Push: Agrega un nuevo elemento a la parte superior (top).
   - Pop: Elimina el elemento que se encuentra en la parte superior.

2. EXPLICACIÓN VISUAL Y DE PROGRAMACIÓN
   Como se muestra en las láminas, un programa de computadora es la
   unión de Estructuras de Datos + Algoritmos.

   - Estructura de Datos: Organiza los datos para una inserción y
     extracción efectiva.
   - Algoritmo: Es el procedimiento paso a paso para resolver el problema.

3. EJEMPLOS DE LA VIDA REAL Y APLICACIONES
   - Mundo Físico: Pila de platos, libros, monedas o papas Pringles.
   - Navegadores Web: El historial (botón "Atrás") es un pop del top.
   - Editores de Texto: La función "Deshacer" (Undo) revierte la última
     acción guardada en la pila.
   - Lógica de Estacionamiento: En un callejón sin salida, los últimos
     en entrar deben salir primero.
======================================================================
"""

class Stack:
    def __init__(self):
        # En Python, una lista es ideal para implementar una pila
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, elemento):
        """Algoritmo: Inserta un dato en la cima (Top)"""
        self._items.append(elemento)
        print(f"PUSH -> '{elemento}' ha sido apilado.")

    def pop(self):
        """Algoritmo: Extrae el dato de la cima (LIFO)"""
        if self.is_empty():
            print("Error: La pila está vacía (Underflow).")
            return None
        extraido = self._items.pop()
        print(f"POP  <- '{extraido}' ha sido retirado.")
        return extraido

    def mostrar_pila(self):
        print(f"\nESTADO ACTUAL: {self._items} <--- TOP\n")

# --- EJECUCIÓN DE EJEMPLOS ---

if __name__ == "__main__":
    # Creando la estructura
    mi_pila = Stack()

    # Ejemplo: Navegador Web (Historial)
    print("--- EJEMPLO: NAVEGADOR WEB ---")
    mi_pila.push("google.com")
    mi_pila.push("youtube.com")
    mi_pila.push("github.com")
    mi_pila.mostrar_pila()

    print("Usuario presiona el botón 'ATRÁS':")
    mi_pila.pop()
    mi_pila.mostrar_pila()

    # Ejemplo: Estacionamiento (Callejón)
    print("--- EJEMPLO: ESTACIONAMIENTO (Callejón 2.3) ---")
    estacionamiento = Stack()
    estacionamiento.push("Auto 2")
    estacionamiento.push("Auto 3")
    estacionamiento.push("Auto 1") # El último en entrar

    print("\nPara que el 'Auto 2' salga, primero deben salir los de arriba:")
    estacionamiento.pop() # Sale el 1
    estacionamiento.pop() # Sale el 3
    estacionamiento.pop() # Sale el 2