def coin_change_limited(wallet, amount):
    changes = []
    wallet.sort(reverse=True)

    for coin in wallet:
        if amount >= coin:
            amount -= coin
            changes.append(coin)

    return changes, amount

if __name__ == "__main__":
    billetera = [500, 100, 50, 50, 50, 10, 10]
    objetivo = 710

    resultado, restante = coin_change_limited(billetera, objetivo)

    print("--- EJERCICIO BILLETERA LIMITADA ---")
    print(f"Monedas seleccionadas: {resultado}")
    print(f"Número de monedas: {len(resultado)}")

    if restante == 0:
        print("¡Cambio completado con éxito!")
    else:
        print(f"No hubo suficientes monedas. Faltaron: {restante} wons.")