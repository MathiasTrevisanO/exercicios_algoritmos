import timeit
import random 

class Queue:
    def __init__(self):
        self.items = []
        self.size = 0
        self.size_limit = 5
    
    def dequeue(self, n):
        if self.size == 0:
            return None
        for _ in range(min(n, self.size)):
            self.items.pop(0)
        self.size -= min(n, self.size)
            
    def _resize(self):
        new_size = self.size_limit * 2
        new_items = self.items[:self.size_limit]
        self.items = new_items
        self.size_limit = new_size
        return self.size_limit
    
    def enqueue(self, value):
        self.items.append(value)
        self.size += 1
        if self.size == self.size_limit:
            self.size_limit = self._resize()
    
def main():
    sizes = [100, 1000, 10000]
    for size in sizes:
        queue = Queue()
        for _ in range(size):
            queue.enqueue(random.randint(1, 100))
        
        n_operations = 1000
        total_time = timeit.timeit(lambda: queue.dequeue(n_operations), number= 1)
        avg_time = total_time / n_operations    

        print(f"Queue size: {size}, Mean Dequeue Cost: {avg_time:.10f} seconds")
    
    
if __name__ == '__main__':
    main()
