books = [
    "The Little Prince", "The Old Man and the Sea", "The Little Mermaid",
    "Beauty and the Beast", "The Last Leaf", "Alice in WonderLand"
]
table = [None] * 10

for book in books:
    key = sum(map(ord, book))
    index = key % 10
    table[index] = book

for i, content in enumerate(table):
    if content:
        print(f"Compartimento {i}: {content}")