# --- EJERCICIO 1: EL EMPLEADO Y EL BONO (Herencia y Polimorfismo) ---
# Enunciado: Crea una clase 'Empleado' con nombre y salario.
# Luego, una clase 'Gerente' que herede de ella y añada un bono al salario.

# Traducción:
# "Create a base class Employee. Then a subclass Manager that
# overrides the 'get_salary' method to include a performance bonus."

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def obtener_salario(self):
        return self.salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, bono):
        # Usamos super() para no repetir el código del padre
        super().__init__(nombre, salario)
        self.bono = bono

    def obtener_salario(self):
        # Polimorfismo: el mismo método funciona distinto para el Gerente
        return self.salario + self.bono

# Prueba Ejercicio 1
emp = Empleado("Ana", 2000)
ger = Gerente("Carlos", 3000, 500)

print(f"Salario de Ana: {emp.obtener_salario()}€")
print(f"Salario de Carlos (con bono): {ger.obtener_salario()}€")