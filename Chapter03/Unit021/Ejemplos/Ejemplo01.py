"""
GUÍA DE PROGRAMACIÓN ORIENTADA A OBJETOS (POO) EN PYTHON
Conceptos: Clases, Objetos, Atributos y Métodos.
"""

# 1. DEFINICIÓN DE UNA CLASE
# Una clase es un "plano" o "molde" para crear objetos.
# Por convención, usamos CapWords (PascalCase).

class CuentaBancaria:
    """
    Esta clase es la evolución de la closure que hicimos antes.
    """

    # El método __init__ es el CONSTRUCTOR.
    # Se ejecuta automáticamente al crear un objeto.
    def __init__(self, titular, saldo_inicial):
        # 'self' es una referencia al objeto específico que estamos creando.
        # Los atributos (datos) se guardan en el objeto usando self.
        self.titular = titular  # Atributo público
        self.saldo = saldo_inicial
        self._numero_cuenta = "ES12345" # Atributo 'protegido' (convención)

    # Los MÉTODOS son funciones que pertenecen a la clase.
    def depositar(self, cantidad):
        self.saldo += cantidad
        return f"Ingreso: +{cantidad}. Saldo actual: {self.saldo}"

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return "Fondos insuficientes."
        self.saldo -= cantidad
        return f"Retiro: -{cantidad}. Saldo actual: {self.saldo}"

    def __str__(self):
        """Método especial para decidir qué se imprime al hacer print(objeto)"""
        return f"Cuenta de {self.titular} - Saldo: {self.saldo}€"


# 2. INSTANCIACIÓN (Crear objetos a partir del molde)

# 'mi_cuenta' es una INSTANCIA de la clase CuentaBancaria
mi_cuenta = CuentaBancaria("Alex", 1000)
cuenta_amigo = CuentaBancaria("Juan", 50)

# 3. USO DE LOS MÉTODOS Y ATRIBUTOS

print(f"Titular: {mi_cuenta.titular}") # Acceder a un atributo
print(mi_cuenta.depositar(500))        # Llamar a un método
print(mi_cuenta)                       # Gracias al método __str__


# --- COMPARATIVA: CLOSURE vs CLASE ---

"""
¿Por qué usar Clases en vez de Closures?
1. Escalabilidad: Es más fácil añadir 20 métodos a una clase que a una closure.
2. Herencia: Las clases pueden heredar funciones de otras clases.
3. Claridad: La sintaxis 'objeto.metodo()' es muy intuitiva.
"""

# Ejemplo rápido de HERENCIA (Un concepto que suele seguir a las clases)
class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo, interes=0.02):
        # Llamamos al constructor del padre (CuentaBancaria)
        super().__init__(titular, saldo)
        self.interes = interes

    def aplicar_interes(self):
        ganancia = self.saldo * self.interes
        self.saldo += ganancia
        return f"Intereses aplicados: +{ganancia}. Total: {self.saldo}"

# Prueba de herencia
ahorro = CuentaAhorro("Lucia", 2000)
print(ahorro.depositar(100)) # Usa el método del padre
print(ahorro.aplicar_interes()) # Usa su propio método