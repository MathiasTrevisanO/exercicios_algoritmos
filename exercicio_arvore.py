class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def height(self):
        return self.recursive_height(self.root)

    def recursive_height(self, current_node):
        if current_node is None:
            return -1
        else:
            left_height = self.recursive_height(current_node.left)
            right_height = self.recursive_height(current_node.right)
            return 1 + max(left_height, right_height)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._recursive_insert(self.root, value)

    def _recursive_insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._recursive_insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._recursive_insert(current_node.right, value)

    def in_order_traversal(self, callback):
        self._in_order_traversal(self.root, callback)

    def _in_order_traversal(self, current_node, callback):
        if current_node is not None:
            self._in_order_traversal(current_node.left, callback)
            callback(current_node.value)
            self._in_order_traversal(current_node.right, callback)
    
    def pre_order_traversal(self, callback):
        self._pre_order_traversal(self.root, callback)
    
    def _pre_order_traversal(self, current_node, callback):
        if current_node is not None:
            callback(current_node.value)
            self._pre_order_traversal(current_node.left, callback)
            self._pre_order_traversal(current_node.right, callback)
    
    def post_order_traversal(self, callback):
        self._post_order_traversal(self.root, callback)
    
    def _post_order_traversal(self, current_node, callback):
        if current_node is not None:
            self._post_order_traversal(current_node.left, callback)
            self._post_order_traversal(current_node.right, callback)
            callback(current_node.value)

    def print_in_order(self, callback):
        if self.root is not None:
            values = []
            self._print_in_order(self.root, callback, values)
            return values

    def _print_in_order(self, current_node, callback, values):
        if current_node is not None:
            self._print_in_order(current_node.left, callback, values)
            values.append(current_node.value)
            self._print_in_order(current_node.right, callback, values)

    def print_pre_order(self, callback):
        if self.root is not None:
            values = []
            self._print_pre_order(self.root, callback, values)
            return values
    
    
    def _print_pre_order(self, current_node, callback, values):
        if current_node is not None:
            values.append(current_node.value)
            self._print_pre_order(current_node.left, callback, values)
            self._print_pre_order(current_node.right, callback, values)
    
    def print_post_order(self, callback):
        if self.root is not None:
            values = []
            self._print_post_order(self.root, callback, values)
            return values
    
    def _print_post_order(self, current_node, callback, values):
        if current_node is not None:
            self._print_post_order(current_node.left, callback, values)
            self._print_post_order(current_node.right, callback, values)
            values.append(current_node.value)


def main():
    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    in_order_values = tree.print_in_order(tree.root)
    print("Tree in order:\n", in_order_values)

    pre_order_values = tree.print_pre_order(tree.root)
    print("Tree pre order:\n", pre_order_values)

    post_order_values = tree.print_post_order(tree.root)
    print("Tree post order:\n", post_order_values)

    print("Height of the tree:", tree.height())

if __name__ == "__main__":
    main()
