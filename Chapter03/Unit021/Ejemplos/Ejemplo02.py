"""
POO: CLASES, INSTANCIAS Y EL MÉTODO __INIT__
Este script resume la estructura profesional de una clase en Python.
"""

# 1. LA CLASE (EL MOLDE)
# Según tus diapositivas, la clase define el estado (datos)
# y el comportamiento (funciones).

class Persona:
    """
    Atributo de Clase: Compartido por todas las instancias.
    """
    especie = "Homo Sapiens"

    # 2. EL CONSTRUCTOR (__init__)
    # Es el método que "inicializa" el objeto.
    def __init__(self, nombre, edad):
        # Atributos de Instancia: Únicos para cada objeto.
        self.nombre = nombre  # self hace referencia al objeto actual
        self.edad = edad

    # 3. MÉTODOS DE INSTANCIA
    # Representan las acciones que el objeto puede realizar.
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

    def cumplir_años(self):
        self.edad += 1
        return f"¡Felicidades {self.nombre}! Ahora tienes {self.edad}."

# 4. INSTANCIACIÓN (CREAR OBJETOS)
# Aquí creamos "ejemplares" reales basados en el molde.

p1 = Persona("Ana", 25)
p2 = Persona("Luis", 30)

# 5. ACCESO A DATOS Y COMPORTAMIENTO
print(p1.saludar())
print(p2.cumplir_años())


# --- CONCEPTOS CLAVE DE TUS IMÁGENES ---

"""
A) SELF: 
Es como el "DNI" del objeto. Permite que el método sepa 
exactamente sobre qué datos trabajar. Sin 'self', no puedes
acceder a los atributos de la instancia.

B) ATRIBUTOS vs MÉTODOS:
- Atributos: Lo que el objeto TIENE (Variables).
- Métodos: Lo que el objeto HACE (Funciones).

C) ESTADO DEL OBJETO:
Es el valor actual de sus atributos en un momento dado. 
Al llamar a cumplir_años(), cambiamos el 'estado' de la edad.
"""

# EJERCICIO DE REPASO:
# Crea una clase 'Coche' con marca y modelo, y un método 'arrancar'.

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    def arrancar(self):
        self.encendido = True
        return f"El {self.marca} {self.modelo} ha arrancado."

mi_coche = Coche("Toyota", "Corolla")
print(mi_coche.arrancar())