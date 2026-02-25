# --- EJERCICIO 4: ORDEN DE BÚSQUEDA LEGB (Reto de Scopes) ---
# Enunciado: ¿Qué imprimirá este código basándonos en la jerarquía?
# (Basado en la imagen image_249b03.png)

x = "Global"

def exterior():
    x = "Enclosing"

    def interior():
        # Descomenta una línea a la vez para probar:
        # x = "Local"
        print(f"El valor de x que encuentro es: {x}")

    interior()

print("\n--- Reto LEGB ---")
exterior()