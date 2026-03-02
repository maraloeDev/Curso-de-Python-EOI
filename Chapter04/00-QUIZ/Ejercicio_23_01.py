class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item) # Entra por el final

    def dequeue(self):
        # Sale el primero (índice 0) - Lógica FIFO
        return self.queue.pop(0) if len(self.queue) > 0 else None

q = Queue()
q.enqueue("Banana")     # ["Banana"]
q.enqueue("Apple")      # ["Banana", "Apple"]
q.enqueue("Tomato")     # ["Banana", "Apple", "Tomato"]
q.dequeue()             # Sale "Banana" -> ["Apple", "Tomato"]
q.enqueue("Strawberry") # ["Apple", "Tomato", "Strawberry"]
q.enqueue("Grapes")     # ["Apple", "Tomato", "Strawberry", "Grapes"]
q.dequeue()             # Sale "Apple" -> ["Tomato", "Strawberry", "Grapes"]

print(f"Salida 23-01: {q.queue}")