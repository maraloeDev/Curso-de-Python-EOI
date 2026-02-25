# --- EJERCICIO 2: EL VEHÍCULO PROTEGIDO (Encapsulamiento) ---
# Enunciado: Crea una clase 'Coche' que proteja su kilometraje.
# No se debe poder bajar el kilometraje, solo aumentarlo.

# Traducción:
# "Create a Car class with a private attribute '__mileage'.
# Implement a method to 'drive' that adds distance,
# ensuring mileage never decreases."

class Coche:
    def __init__(self, marca):
        self.marca = marca
        self.__kilometraje = 0  # Atributo privado

    def conducir(self, km):
        if km > 0:
            self.__kilometraje += km
            return f"Kilometraje actualizado: {self.__kilometraje} km"
        else:
            return "¡Error! No puedes quitarle kilómetros al coche."

    def mostrar_info(self):
        return f"Coche: {self.marca} | Odo: {self.__kilometraje} km"

# Prueba Ejercicio 2
mi_coche = Coche("Toyota")
print(mi_coche.conducir(100))
print(mi_coche.conducir(-50)) # Intento de fraude
print(mi_coche.mostrar_info())