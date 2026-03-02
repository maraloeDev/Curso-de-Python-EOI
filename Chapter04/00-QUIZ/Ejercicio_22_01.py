class Stack:
    def __init__(self):
        self.stack = [] # Lista interna para guardar datos

    def push(self, item):
        self.stack.append(item) # Añade al final

    def pop(self):
        # Saca el último si hay elementos
        return self.stack.pop() if len(self.stack) > 0 else None

s = Stack()
s.push("Banana")     # Pila: ["Banana"]
s.push("Apple")      # Pila: ["Banana", "Apple"]
s.push("Tomato")     # Pila: ["Banana", "Apple", "Tomato"]
s.pop()              # Quita "Tomato" -> ["Banana", "Apple"]
s.push("Strawberry") # Pila: ["Banana", "Apple", "Strawberry"]
s.push("Grapes")     # Pila: ["Banana", "Apple", "Strawberry", "Grapes"]
s.pop()              # Quita "Grapes" -> ["Banana", "Apple", "Strawberry"]

print(f"Salida 22-01: {s.stack}")