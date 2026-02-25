from collections import deque

class Cola:
    def __init__(self, nombre):
        self.items = deque()
        self.nombre = nombre

    def enqueue(self, item):
        self.items.append(item)
        print(f"[{self.nombre}] Llegó: {item}")

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.popleft()
        return None

# --- Simulación ---
peaje = Cola("Peaje Autopista")
peaje.enqueue("Auto Rojo")
peaje.enqueue("Auto Azul")
peaje.enqueue("Auto Verde")

print("\n--- Procesando vehículos ---")
while len(peaje.items) > 0:
    vehiculo = peaje.dequeue()
    print(f"El {vehiculo} pagó y salió.")