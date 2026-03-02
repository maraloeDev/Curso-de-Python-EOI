low, high = 1, 100
target = 25
count = 0

while low < high:
    mid = (low + high) // 2
    count += 1
    if mid == target:
        break
    elif mid > target:
        high = mid - 1
    else:
        low = mid + 1

print(f"Salida 25-02 (Intentos para 25): {count}")