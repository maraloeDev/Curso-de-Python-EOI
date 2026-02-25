from collections import deque

class ColaImpresion:
    def __init__(self):
        self.trabajos = deque()

    def enviar_documento(self, doc):
        self.trabajos.append(doc)
        print(f"Documento '{doc}' enviado a la cola.")

    def imprimir_siguiente(self):
        if len(self.trabajos) > 0:
            doc = self.trabajos.popleft()
            print(f"IMPRIMIENDO: {doc}... [OK]")
        else:
            print("No hay documentos pendientes.")

# --- Simulación ---
impresora = ColaImpresion()
impresora.enviar_documento("Tarea_Mate.pdf")
impresora.enviar_documento("Foto_Perfil.png")

print("\n--- Iniciando Impresión ---")
impresora.imprimir_siguiente()
impresora.imprimir_siguiente()