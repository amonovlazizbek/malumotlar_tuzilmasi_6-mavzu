class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        if self.is_full():
            print("Navbat to`la:", value)
            return

        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print(" Navbat bo`sh")
            return None

        value = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return value

    def display(self):
        if self.is_empty():
            print("Navbat bo`sh")
            return

        i = self.front
        result = []

        while True:
            result.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size

        print("Navbat:", result)


cq = CircularQueue(6)  
cq.enqueue("A")
cq.enqueue("B")
cq.enqueue("C")
cq.enqueue("D")
cq.enqueue("E")

cq.display()

cq.dequeue()
cq.dequeue()
cq.dequeue()

cq.display()
cq.enqueue("F")
cq.enqueue("G")

# 🔹 Natija
cq.display()
