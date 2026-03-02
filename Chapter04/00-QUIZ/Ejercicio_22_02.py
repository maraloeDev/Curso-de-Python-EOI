stack = []
items = [10 * i for i in range(1, 10)]

for item in items:
    stack.append(item) # Push

    if (item // 10) % 2 == 0:
        stack.pop()

print(f"Salida 22-02: {stack}")
