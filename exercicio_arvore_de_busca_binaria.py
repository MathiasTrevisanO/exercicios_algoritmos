class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)
    
    def insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self.insert_recursive(current_node.right, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self.insert_recursive(current_node.right, value)
    
    def verify_value(self, value):
        return self.verify_value_recursive(self.root, value)
    
    def verify_value_recursive(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self.verify_value_recursive(current_node.left, value)
        else:
            return self.verify_value_recursive(current_node.right, value)

def main():
    tree = BST()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(12)
    tree.insert(17)
    
    value1 = 12
    value2 = 5
    
    print(tree.verify_value(value1))
    print(tree.verify_value(value2))
        
if __name__ == '__main__':
    main()
                
            
            