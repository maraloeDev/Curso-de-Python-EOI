from collections import deque

class Cola:
    def __init__(self, nombre="Cola"):
        self.items = deque()
        self.nombre = nombre

    def enqueue(self, item):
        self.items.append(item)
        print(f"[{self.nombre}] ENQUEUE: '{item}' entró.")

    def dequeue(self):
        if not self.is_empty():
            item = self.items.popleft()
            print(f"[{self.nombre}] DEQUEUE: '{item}' salió.")
            return item
        return None

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return f"{self.nombre}: {list(self.items)}"

# Prueba rápida
if __name__ == "__main__":
    c = Cola("Test")
    c.enqueue("Dato 1")
    c.enqueue("Dato 2")
    c.dequeue()
    print(c)