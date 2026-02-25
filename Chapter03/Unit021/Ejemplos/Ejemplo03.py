"""
POO AVANZADA: HERENCIA, COMPOSICIÓN Y MÉTODOS ESPECIALES
Este script explica cómo reutilizar código y organizar clases complejas.
"""

# 1. HERENCIA (Inheritance)
# Permite que una clase (hija) herede atributos y métodos de otra (padre).

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.en_marcha = False

    def arrancar(self):
        self.en_marcha = True
        return f"{self.marca} {self.modelo} ha arrancado."

# La clase Coche "Hereda" de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, combustible):
        # super() llama al constructor del padre
        super().__init__(marca, modelo)
        self.combustible = combustible

    def tocar_claxon(self):
        return "¡Beep beep!"

# 2. COMPOSICIÓN (Composition)
# En lugar de "ser" algo (herencia), el objeto "tiene" algo.
#

class Motor:
    def __init__(self, cilindrada):
        self.cilindrada = cilindrada

class Camion(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        # El Camión TIENE un Motor (Composición)
        self.motor = Motor(5000)

    # 3. MÉTODOS DE CLASE Y ESTÁTICOS (@classmethod y @staticmethod)
# A veces no necesitamos acceder a una instancia específica (self).

class Utilidades:
    factor_conversion = 1.609

    @staticmethod
    def limpiar_texto(texto):
        """No necesita saber nada de la clase ni del objeto."""
        return texto.strip().capitalize()

    @classmethod
    def millas_a_km(cls, millas):
        """Accede a la clase (cls) para usar sus atributos."""
        return millas * cls.factor_conversion


# --- TRADUCCIÓN DE CONCEPTOS CLAVE ---

conceptos = {
    "Inheritance": "Herencia - Una clase hija toma lo de la clase padre.",
    "Polymorphism": "Polimorfismo - Un mismo método se comporta distinto en clases diferentes.",
    "Encapsulation": "Encapsulamiento - Agrupar datos y métodos restringiendo el acceso.",
    "Abstraction": "Abstracción - Ocultar los detalles complejos y mostrar solo lo necesario."
}

# --- PRUEBA DE CÓDIGO ---

if __name__ == "__main__":
    print("--- Ejemplo de Herencia ---")
    mi_coche = Coche("Ford", "Mustang", "Gasolina")
    print(mi_coche.arrancar())
    print(mi_coche.tocar_claxon())

    print("\n--- Ejemplo de Métodos de Clase ---")
    print(f"10 millas son: {Utilidades.millas_a_km(10)} km")
    print(Utilidades.limpiar_texto("   hola mundo   "))