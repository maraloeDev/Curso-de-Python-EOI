def coin_change(coins, amount):
    """
    Implementación del algoritmo codicioso para el cambio de monedas.
    Selecciona siempre la moneda más grande disponible.
    """
    changes = []
    # El algoritmo asume que las monedas están ordenadas de mayor a menor
    sorted_coins = sorted(coins, reverse=True)

    for coin in sorted_coins:
        while amount >= coin:
            amount -= coin
            changes.append(coin)
    return changes

if __name__ == "__main__":
    # Configuración del ejercicio Q1
    coins_q1 = [500, 400, 100, 50, 10]
    amount_q1 = 800

    # Ejecución del algoritmo
    result = coin_change(coins_q1, amount_q1)

    print("--- RESULTADO EJERCICIO Q1 ---")
    print(f"Monedas disponibles: {coins_q1}")
    print(f"Cantidad a devolver: {amount_q1}")
    print(f"Salida del algoritmo: {result}, {len(result)}")
