"""
1. DEFINICIÓN Y CONCEPTOS FUNDAMENTALES
   Una Cola (Queue) es una estructura de datos lineal que sigue el principio
   FIFO (First-In-First-Out): el primero en entrar es el primero en salir.

   Operaciones Principales:
   - Enqueue: Agrega un elemento al final (Rear) de la cola.
   - Dequeue: Elimina el elemento que está al frente (Front) de la cola.
   - Peek/Front: Observa el primer elemento sin eliminarlo.
"""

from collections import deque

class Cola:
    def __init__(self):
        # Usamos deque por ser más eficiente que una lista para eliminar del inicio
        self.items = deque()

    def esta_vacia(self):
        return len(self.items) == 0

    def enqueue(self, item):
        """Agrega un elemento al final de la fila."""
        self.items.append(item)
        print(f"[ENQUEUE]: '{item}' entró a la cola.")

    def dequeue(self):
        """Elimina el primer elemento que llegó."""
        if not self.esta_vacia():
            item = self.items.popleft()
            print(f"[DEQUEUE]: '{item}' salió de la cola.")
            return item
        print("Error: La cola está vacía.")
        return None

    def __str__(self):
        return f"Estado de la Cola: {list(self.items)} <- Final"

if __name__ == "__main__":
    fila_banco = Cola()
    fila_banco.enqueue("Cliente 1")
    fila_banco.enqueue("Cliente 2")
    print(fila_banco)
    fila_banco.dequeue()
    print(fila_banco)