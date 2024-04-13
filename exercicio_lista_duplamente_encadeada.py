class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, value):
        new_value = Node(value)
        if self.head is None:
            self.head = new_value
            self.tail = new_value
        else:
            self.tail.next = new_value
            new_value.prev = self.tail
            self.tail = new_value

    def prepend(self, value):
        new_value = Node(value)
        if self.head is None:
            self.head = new_value
            self.tail = new_value
        else:
            new_value.next = self.head
            self.head.prev = new_value
            self.head = new_value
    
    def remove(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                if current.prev is not None:
                    current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                break
            current = current.next
        return current
    
    def print_list(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        print(" <-> ".join(elements))
    

dll = DoubleLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

dll.prepend(5)

print("List of doubles linked list:")
dll.print_list()

dll.remove(20)

print("\nList after removed:")
dll.print_list()
