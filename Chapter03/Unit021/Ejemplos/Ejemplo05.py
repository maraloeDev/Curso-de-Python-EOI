"""
POO: LOS 4 PILARES Y MÉTODOS DE NIVEL SUPERIOR
Este script resume la teoría final sobre Abstracción, Encapsulamiento,
Herencia y Polimorfismo.
"""

# 1. ENCAPSULAMIENTO (Encapsulation)
# Según tus imágenes, sirve para restringir el acceso a los datos.
# En Python, usamos el guion bajo "_" para indicar que es "privado".

class Smartphone:
    def __init__(self, marca, nivel_bateria):
        self.marca = marca          # Público
        self.__bateria = nivel_bateria # Privado (Dunder score)

    def usar(self):
        if self.__bateria > 0:
            self.__bateria -= 10
            return f"Usando {self.marca}. Batería al {self.__bateria}%"
        return "Sin batería."

    # Getter para ver la batería sin modificarla directamente
    def ver_bateria(self):
        return f"Carga actual: {self.__bateria}%"


# 2. ABSTRACCIÓN (Abstraction)
# Consiste en ocultar la complejidad interna y mostrar solo lo necesario.
#



class Cafetera:
    def __init__(self):
        self._temperatura = 0

    def hacer_cafe(self):
        # El usuario solo ve este método, no los 3 pasos internos
        self._calentar_agua()
        self._moler_grano()
        return "☕ Café listo."

    def _calentar_agua(self):
        self._temperatura = 90

    def _moler_grano(self):
        pass


# 3. POLIMORFISMO (Polymorphism)
# Varias clases pueden tener un método con el mismo nombre pero que hace cosas distintas.
#

class Perro:
    def hablar(self): return "¡Guau!"

class Gato:
    def hablar(self): return "¡Miau!"

def emitir_sonido(animal):
    # No importa qué animal sea, Python sabe qué 'hablar' usar
    print(animal.hablar())


# 4. MÉTODOS DE CLASE (@classmethod)
# Se usan para cosas que afectan a toda la clase, no a un objeto concreto.
#

class Empresa:
    nombre_empresa = "Python S.A."

    @classmethod
    def cambiar_nombre(cls, nuevo_nombre):
        cls.nombre_empresa = nuevo_nombre
        return f"Ahora somos {cls.nombre_empresa}"


# --- RESUMEN DE LOS 4 PILARES (Traducción) ---

resumen = {
    "Abstracción": "Ocultar detalles complicados. Solo importa 'qué hace', no 'cómo'.",
    "Encapsulamiento": "Mantener los datos seguros dentro del objeto.",
    "Herencia": "Reutilizar código creando una clase nueva a partir de otra.",
    "Polimorfismo": "Un mismo nombre de función para diferentes tipos de objetos."
}

# --- PRUEBA DEL CÓDIGO ---

if __name__ == "__main__":
    print("--- 1. Encapsulamiento ---")
    movil = Smartphone("Xiaomi", 100)
    print(movil.usar())

    print("\n--- 2. Polimorfismo ---")
    emitir_sonido(Perro())
    emitir_sonido(Gato())

    print("\n--- 3. Método de Clase ---")
    print(Empresa.cambiar_nombre("Tech Solutions"))