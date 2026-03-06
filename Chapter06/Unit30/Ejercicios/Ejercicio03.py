def coin_change2(coins, amount):
    changes = []

    for coin in coins:
        # Si la moneda cabe en el monto restante, se toma
        if amount >= coin:
            amount -= coin
            changes.append(coin)

    return changes

if __name__ == "__main__":

    # Entrada simulada: 500 50 50 100 50 10 10
    coins = [500, 50, 50, 100, 50, 10, 10]
    print(f"Input the coins: {' '.join(map(str, coins))}")

    # 2. Lo ordeno de manera descendente
    coins.sort(reverse=True)
    print(coins)

    # 3. Introduzco el monto a devolver
    amount = 710
    print(f"Input the amount: {amount}")

    # 4. Cálculo del cambio
    changes = coin_change2(coins, amount)

    # 5. Resultado final
    print(f"{changes} {len(changes)}")