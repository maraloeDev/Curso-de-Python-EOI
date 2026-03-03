comparaciones = 0

def merge_eficiente(S, low, mid, high):
    global comparaciones
    temp = []
    i, j = low, mid + 1

    while i <= mid and j <= high:
        comparaciones += 1
        if S[i] < S[j]:
            temp.append(S[i]); i += 1
        else:
            temp.append(S[j]); j += 1

    while i <= mid: temp.append(S[i]); i += 1
    while j <= high: temp.append(S[j]); j += 1

    for k in range(len(temp)):
        S[low + k] = temp[k]

def mergesort_eficiente(S, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort_eficiente(S, low, mid)
        mergesort_eficiente(S, mid + 1, high)
        merge_eficiente(S, low, mid, high)

datos = [27, 10, 12, 20, 25, 13, 15, 22]
print(f"Lista original: {datos}")
mergesort_eficiente(datos, 0, len(datos) - 1)
print(f"Lista ordenada: {datos}")
print(f"Total de comparaciones con la balanza: {comparaciones}")