"""
======================================================================
           RESUMEN: ESTRUCTURA DE DATOS - COLA (QUEUE)
======================================================================

1. DEFINICIÓN Y CONCEPTOS FUNDAMENTALES
   Una Cola (Queue) es un tipo de dato abstracto lineal donde los
   elementos se gestionan bajo el principio FIFO (First-In-First-Out).
   Esto significa que el primer elemento en entrar es el primero en salir.

   Operaciones Principales:
   - Enqueue (Encolar): Agrega un elemento al final (Rear) de la cola.
   - Dequeue (Desencolar): Elimina el elemento que está al frente (Front).

2. EXPLICACIÓN DE PROGRAMACIÓN
   Al igual que el Stack, la Cola es una estructura definida por el
   usuario para organizar datos de manera eficiente.
   - Front: Es el extremo por donde salen los datos.
   - Rear: Es el extremo por donde entran los datos.

3. EJEMPLOS MÁS UTILIZADOS
   - Mundo Físico: Fila en el banco, fila para el cine, fila de espera.
   - Informática:
     * Buffer de teclado (guarda las teclas en orden mientras el CPU procesa).
     * Colas de impresión (imprime los documentos según llegaron).
     * Servidores de streaming (el video se carga en una cola de paquetes).
======================================================================
"""

from collections import deque

class Cola:
    def __init__(self, nombre="Fila"):
        # Se usa deque (double-ended queue) porque es mucho más rápido
        # que una lista normal para eliminar elementos del inicio.
        self.items = deque()
        self.nombre = nombre

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, elemento):
        """Agrega un elemento al final."""
        self.items.append(elemento)
        print(f"[{self.nombre}] ENQUEUE: '{elemento}' entró a la fila.")

    def dequeue(self):
        """Elimina el elemento del frente (el más antiguo)."""
        if self.is_empty():
            print(f"[{self.nombre}] Error: Underflow (Cola vacía).")
            return None
        extraido = self.items.popleft()
        print(f"[{self.nombre}] DEQUEUE: '{extraido}' fue atendido y salió.")
        return extraido

    def front(self):
        """Mira quién es el primero sin sacarlo."""
        return self.items[0] if not self.is_empty() else None

    def __str__(self):
        return f"ESTADO {self.nombre.upper()}: {list(self.items)} <--- Final"

# --- CASOS DE PRÁCTICA ---

if __name__ == "__main__":
    # Caso 1: Fila del Banco
    print("--- SIMULACIÓN: BANCO ---")
    banco = Cola("Banco Central")
    banco.enqueue("Cliente 1")
    banco.enqueue("Cliente 2")
    banco.enqueue("Cliente 3")

    print(f"\nSiguiente en el frente: {banco.front()}")
    banco.dequeue() # Sale el Cliente 1
    print(banco)

    print("\n" + "-"*30 + "\n")

    # Caso 2: Cola de Impresión
    print("--- SIMULACIÓN: IMPRESORA ---")
    impresora = Cola("HP_LaserJet")
    impresora.enqueue("Tesis_Parte1.pdf")
    impresora.enqueue("Foto_Gato.png")

    print(f"Imprimiendo ahora: {impresora.dequeue()}")
    print(impresora)