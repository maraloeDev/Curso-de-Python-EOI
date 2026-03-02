queue = []
items = [10 * i for i in range(1, 11)]

for item in items:
    queue.append(item) # Enqueue
    # Si la decena es par (20, 40, 60, 80, 100), se saca el primero de la cola
    if (item // 10) % 2 == 0:
        queue.pop(0) # Dequeue

print(f"Salida 23-02: {queue}")