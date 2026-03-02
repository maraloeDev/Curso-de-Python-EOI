def find_two(nums):
    x = y = 0 # Inicializamos índices en 0
    for i in range(1, len(nums)):
        if nums[x] < nums[i]: # Busca el índice del mayor
            x = i
        if nums[y] > nums[i]: # Busca el índice del menor
            y = i
    return x, y

nums = [11, 37, 45, 26, 59, 28, 17, 53]
i, j = find_two(nums)
print(f"Resultado 24-01: Mayor={nums[i]}, Menor={nums[j]}")