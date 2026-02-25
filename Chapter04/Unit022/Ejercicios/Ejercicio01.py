"""
1. DEFINICIÓN Y CONCEPTOS FUNDAMENTALES (Basado en Láminas 1.1 y 2.1)
- Stack (Pila): Tipo de dato abstracto (ADT) lineal.
- LIFO: Last-In-First-Out (Último en entrar, primero en salir).
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        """Lámina 2.1: Agrega un nuevo ítem en el top."""
        self.items.append(item)

    def pop(self):
        """Lámina 2.1: Remueve un ítem del top."""
        if not self.is_empty():
            return self.items.pop()
        return "Error: Stack vacío"

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def __str__(self):
        return f"Stack actual: {self.items}"

if __name__ == "__main__":
    pila = Stack()
    pila.push("A")
    pila.push("B")
    pila.push("C")
    print(pila) # Salida: ['A', 'B', 'C']