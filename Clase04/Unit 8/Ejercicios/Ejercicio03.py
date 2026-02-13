n = int(input("Enter n : "))

for i in range(n):
    fila = list(range(i * n + 1, (i + 1) * n + 1))
    if i % 2 != 0:
        fila.reverse()
    for num in fila:
        print(f"{num:3}", end=" ")
    print()