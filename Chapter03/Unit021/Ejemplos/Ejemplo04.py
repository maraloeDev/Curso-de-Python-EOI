"""
PILARE DE LA POO Y MÉTODOS DE CLASE
Resumen final de conceptos: Encapsulamiento, Herencia y Polimorfismo.
"""

# 1. ENCAPSULAMIENTO (Encapsulation)
# Protege los datos internos. En Python usamos "_" para indicar que algo
# es "privado" o "protegido".

class SmartPhone:
    def __init__(self, modelo, bateria):
        self.modelo = modelo        # Atributo público
        self.__bateria = bateria    # Atributo privado (Encapsulado)

    def usar(self, gasto):
        if gasto <= self.__bateria:
            self.__bateria -= gasto
            return f"Batería restante: {self.__bateria}%"
        return "Sin batería suficiente."

# 2. HERENCIA Y POLIMORFISMO
# El polimorfismo permite que diferentes clases tengan métodos con el
# mismo nombre pero comportamientos distintos.

class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "¡Guau!"

class Gato(Animal):
    def hablar(self):
        return "¡Miau!"

# Ejemplo de Polimorfismo en acción:
def hacer_ruido(animal):
    print(animal.hablar())


# 3. MÉTODOS DE CLASE (@classmethod) vs MÉTODOS ESTÁTICOS (@staticmethod)
# Según tus imágenes, estos sirven para utilidades que no dependen de
# una instancia específica.

class Constantes:
    PI = 3.14159

    @classmethod
    def info(cls):
        return f"Esta clase maneja constantes matemáticas como {cls.PI}"

    @staticmethod
    def sumar(a, b):
        return a + b

# --- TRADUCCIÓN DE LOS 4 PILARES ---

resumen_pilares = {
    "Abstracción": "Mostrar solo lo necesario del objeto y ocultar la complejidad interna.",
    "Encapsulamiento": "Agrupar datos y métodos, restringiendo el acceso directo a lo interno.",
    "Herencia": "Crear clases nuevas a partir de clases existentes para reutilizar código.",
    "Polimorfismo": "Capacidad de diferentes objetos de responder al mismo mensaje (método) de forma distinta."
}

# --- PRUEBA FINAL ---

if __name__ == "__main__":
    print("--- 1. Polimorfismo ---")
    mascotas = [Perro(), Gato()]
    for m in mascotas:
        hacer_ruido(m)

    print("\n--- 2. Encapsulamiento ---")
    movil = SmartPhone("iPhone 15", 100)
    print(movil.usar(20))
    # print(movil.__bateria)  # <-- Esto daría error, está protegido.

    print("\n--- 3. Métodos de Clase ---")
    print(Constantes.info())