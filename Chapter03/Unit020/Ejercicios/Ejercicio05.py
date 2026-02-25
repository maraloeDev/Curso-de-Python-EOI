# "Crea una clausura que gestione una cuenta bancaria.
# Debe recordar el 'titular' y el 'saldo'.
# Debe permitir depósitos, retiros y evitar saldos negativos."

def crear_cuenta(titular, saldo_inicial):
    # Estas variables están en el 'Enclosing Scope'
    # Se mantendrán vivas gracias a la closure
    nombre = titular
    saldo = saldo_inicial

    def transaccion(tipo, cantidad):
        nonlocal saldo # Necesario para modificar el saldo

        if tipo == "deposito":
            saldo += cantidad
            return f"Ingreso: +{cantidad}. Nuevo saldo de {nombre}: {saldo}"

        elif tipo == "retiro":
            if cantidad > saldo:
                return f"¡Error! Fondos insuficientes para {nombre}."
            saldo -= cantidad
            return f"Retiro: -{cantidad}. Nuevo saldo de {nombre}: {saldo}"

        else:
            return "Operación no válida."

    return transaccion

# --- PRUEBA DEL EJERCICIO ---

# Creamos dos cuentas independientes (cada una tiene su propio scope)
cuenta_paco = crear_cuenta("Paco", 100)
cuenta_maria = crear_cuenta("Maria", 500)

print(cuenta_paco("deposito", 50))   # Salida: Nuevo saldo de Paco: 150
print(cuenta_maria("retiro", 100))   # Salida: Nuevo saldo de Maria: 400
print(cuenta_paco("retiro", 200))    # Salida: ¡Error! Fondos insuficientes...