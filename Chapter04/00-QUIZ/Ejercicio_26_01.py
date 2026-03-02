book = "Alice in WonderLand"
key = sum(map(ord, book)) # Suma valores ASCII: 1763
size = 8
hash_key = key % size

print(f"Salida 26-01: Key={key}, Hash Key={hash_key}")