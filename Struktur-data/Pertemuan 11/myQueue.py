# Membuat MyQueue dari Linked List
# pancingan hijau github
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_node = node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print(f"Data {data} berhasil ditambahkan ke antrean")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        print(f"Dequeued: {data}")
        return data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.head.data

    def is_empty(self):
        return self.size == 0

    def printQueue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# --- Uji Coba Jalankan Program ---
Antrian = Queue()
Antrian.enqueue("andi")
Antrian.enqueue("budi")
Antrian.enqueue("caca")
Antrian.printQueue()