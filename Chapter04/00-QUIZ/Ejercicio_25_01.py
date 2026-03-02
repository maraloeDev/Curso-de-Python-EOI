low, high = 1, 100
target = 51
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

print(f"Salida 25-01 (Intentos para 51): {count}")