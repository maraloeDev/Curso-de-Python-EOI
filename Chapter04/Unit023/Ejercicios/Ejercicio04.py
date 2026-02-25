from collections import deque

class SistemaTickets:
    def __init__(self):
        self.fila = deque()

    def tomar_ticket(self, cliente):
        self.fila.append(cliente)
        print(f"Bienvenido {cliente}, su posición es la #{len(self.fila)}")

    def atender_cliente(self):
        if len(self.fila) > 0:
            cliente = self.fila.popleft()
            print(f"ATENDIENDO A: {cliente}")
        else:
            print("Nadie en espera.")

# --- Simulación ---
banco = SistemaTickets()
banco.tomar_ticket("Juan")
banco.tomar_ticket("Maria")
banco.tomar_ticket("Pedro")

print("\n--- Llamando a ventanilla ---")
banco.atender_cliente()
banco.atender_cliente()