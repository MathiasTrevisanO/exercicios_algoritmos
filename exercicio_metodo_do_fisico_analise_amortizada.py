class Queue:

    def __init__(self):
        self.capacity = 5
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = 0
        self.amortized_cost = 0
        self.resize_count = 0

    def enqueue(self, value):
        if self.size() == self.capacity:
            self._resize()
            self.resize_count += 1
            self.amortized_cost += self.capacity / (2 ** self.resize_count)
        self.queue[self.rear] = value
        self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            raise IndexError("Queue is empty")
        value = self.queue[self.front]
        self.front += 1
        return value

    def size(self):
        return self.rear - self.front

    def _resize(self):
        new_capacity = self.capacity * 2
        new_queue = [None] * new_capacity
        for i in range(self.size()):
            new_queue[i] = self.queue[self.front + i]
        self.queue = new_queue
        self.capacity = new_capacity
        self.front = 0
        self.rear = self.size()

def main():
    q = Queue()
    print("Empty queue?", q.size() == 0)

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)

    print("Queue size after adding 5 items:", q.size() == 5)

    q.enqueue(60)
    q.enqueue(70)
    q.enqueue(80)
    q.enqueue(90)
    q.enqueue(100)
    q.enqueue(110)

    print("Queue size after adding 6 more items:", q.size() == 11)
    print("Amortized cost per enqueue:", q.amortized_cost)

    print("Element removed:", q.dequeue())
    print("Element removed:", q.dequeue())
    print("Element removed:", q.dequeue())

    print("Queue size after removing 3 items:", q.size() == 8)


if __name__ == '__main__':
    main()
