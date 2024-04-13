
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item, priority):
        self.queue.append((priority, item))
        self.heapify_up()
        

    def pop(self):
        priority, item = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop()
        self.heapify_down()
        return item

    def is_empty(self):
        return len(self.queue) == 0
        
        
        
class UnionFindPriority:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.pq = PriorityQueue()
        
    def union(self, p, q):
        p = self.find(p)
        q = self.find(q)
        if self.size[p] < self.size[q]:
            self.parent[p] = q
            self.size[q] += self.size[p]
            self.pq.push(q, self.size[q])
            self.pq.push(p, self.size[p])
        
    def find(self, p):
        if self.parent[p] == p:
            return p
        self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    

def main():
    uf = UnionFindPriority(6)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    
    print(uf.find(0))  # Deve imprimir o líder (representante) do conjunto que contém 0
    print(uf.find(3))  # Deve imprimir o líder (representante) do conjunto que contém 3

    uf.union(1, 3)
    print(uf.find(0))  # Deve imprimir o líder (representante) do conjunto que contém 0 após a união
    print(uf.find(3))  # Deve imprimir o líder (representante) do conjunto que contém 3 após a união

    uf.union(0, 4)
    print(uf.find(4))  # Deve imprimir o líder (representante) do conjunto que contém 4 após a união

    uf.union(5, 2)
    print(uf.find(5))  # Deve imprimir o líder (representante) do conjunto que contém 5 após a união
    print(uf.find(2))  # Deve imprimir o líder (representante) do conjunto que contém 2 após a união

if __name__ == '__main__':
    main()
