def find_two_with_count(nums):
    x = y = 0
    comparison = 0
    for i in range(1, len(nums)):
        if nums[x] < nums[i]: x = i
        if nums[y] > nums[i]: y = i
        comparison += 2

    print(f"Comparaciones totales: {comparison}")
    return x, y

nums = [11, 37, 45, 26, 59, 28, 17, 53]
find_two_with_count(nums) # Para 8 números (n-1 = 7 iteraciones), resultan 14 comparaciones