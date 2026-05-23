#Membuat stack dengan menggunakan linked list
#1.kelas node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#2 kelas stack
class Stack:
    def __init__(self):
        self.top = None  
        self.size = 0

    #METHOD UNTUK NAMBAH STACK    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    #method untuk menampilkan isi stack   
    def display(self):
            current = self.top
            while current:
                print(current.data, end=" <- ")
                current = current.next
            print("None")
    #METHOD UNTUK MENGHAPUS STACK
    def pop(self):
        if self.is_empty():
            return None
        temp = self.top
        self.top = self.top.next
        self.size -= 1
        return temp.data
    
    #METHOD UNTUK MENGECEK APAKAH STACK KOSONG
    def is_empty(self):
        return self.top is None
    
    #METHOD UNTUK MELIHAT STACK TERATAS
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

#PENGGUNAAN STACK
myStack = Stack()
myStack.push(10)
myStack.push(20)
myStack.push(30)
myStack.display() 
myStack.pop()      
myStack.display()  
print(myStack.is_empty())  
print(myStack.peek())