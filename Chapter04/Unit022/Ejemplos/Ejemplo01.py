"""
UNIDAD 22: EL STACK (PILA)
--------------------------

1. DEFINICIÓN Y CONCEPTOS FUNDAMENTALES
   Una Pila (Stack) es un tipo de dato abstracto (ADT) lineal.
   Principio: LIFO (Last-In-First-Out) - El último en entrar es el primero en salir.

   Operaciones Principales:
   - Push: Agrega un elemento al 'top' (cima).
   - Pop: Elimina y devuelve el elemento del 'top'.

2. EXPLICACIÓN DE PROGRAMACIÓN
   Programa = Estructuras de Datos + Algoritmos.
   - Estructura de Datos: Organiza (Stack).
   - Algoritmo: Procedimiento de inserción/extracción.

3. EJEMPLOS DE LA VIDA REAL
   - Físico: Platos, libros, botes de Pringles.
   - Software: Botón "Atrás" del navegador, "Deshacer" (Ctrl+Z) en editores.
   - Lógica: Estacionamiento en callejones sin salida (dead-end).
"""

class Stack:
    def __init__(self):
        # Usamos una lista interna para almacenar los datos
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        """Agrega un nuevo elemento a la parte superior (top)."""
        self.items.append(item)
        print(f"[PUSH]: Agregado '{item}' a la cima.")

    def pop(self):
        """Elimina el elemento en la parte superior."""
        if self.is_empty():
            return "La pila está vacía (Underflow)"
        item = self.items.pop()
        print(f"[POP]: Removido '{item}' de la cima.")
        return item

    def peek(self):
        """Muestra qué hay en el top sin quitarlo."""
        if not self.is_empty():
            return self.items[-1]

    def __str__(self):
        return f"Estado actual de la Pila: {self.items}"

# --- CASO DE USO: HISTORIAL DEL NAVEGADOR ---
print("--- Simulando Navegador Web ---")
browser_stack = Stack()

# El usuario visita páginas (PUSH)
browser_stack.push("google.com")
browser_stack.push("wikipedia.org")
browser_stack.push("github.com")

print(browser_stack)

# El usuario presiona el botón 'Atrás' (POP)
print(f"\nClick en botón 'Atrás'...")
browser_stack.pop()

print(f"Página actual: {browser_stack.peek()}")
print(browser_stack)

# --- CASO DE USO: ESTACIONAMIENTO (Callejón sin salida) ---
print("\n--- Simulando Estacionamiento Estrecho ---")
parking = Stack()
parking.push("Auto 1 (Fondo)")
parking.push("Auto 2")
parking.push("Auto 3 (Salida)")

print("\nPara que el 'Auto 1' salga, primero deben salir los otros:")
parking.pop() # Sale Auto 3
parking.pop() # Sale Auto 2
parking.pop() # Finalmente sale Auto 1