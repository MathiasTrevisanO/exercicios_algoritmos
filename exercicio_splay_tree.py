class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None  # Adicionando o atributo parent

class SplayTree:
    def __init__(self):
        self.root = None

    def zig(self, x):
        """
        Rotaciona x para a raiz
        """
        parent = x.parent
        if parent.left == x:
            parent.left = x.right
            if x.right:
                x.right.parent = parent
            x.right = parent
        else:
            parent.right = x.left
            if x.left:
                x.left.parent = parent
            x.left = parent
        x.parent = parent.parent
        if parent.parent is not None:
            if parent.parent.left == parent:
                parent.parent.left = x
            else:
                parent.parent.right = x
        else:
            self.root = x
        parent.parent = x

    def splay(self, x):
        while x.parent is not None:
            parent = x.parent
            grand_parent = parent.parent
            if grand_parent is None:
                self.zig(x)
            elif grand_parent.left == parent and parent.left == x:
                self.zig(parent)
                self.zig(x)
            elif grand_parent.right == parent and parent.right == x:
                self.zig(parent)
                self.zig(x)
            else:
                self.zig(x)
                self.zig(x)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root
        parent = None
        while current is not None:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                self.splay(current)
                return

        new_node = Node(key)
        new_node.parent = parent
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        self.splay(new_node)

    def search(self, key):
        current = self.root
        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                self.splay(current)
                return True
        return False

    def inorder_traversal(self, node):
        if node is None:
            return []
        return self.inorder_traversal(node.left) + [node.key] + self.inorder_traversal(node.right)

    def print_tree(self):
        print(self.inorder_traversal(self.root))


# Exemplo de uso
if __name__ == "__main__":
    tree = SplayTree()
    keys = [100, 50, 200, 40, 30, 20, 25, 35]
    for key in keys:
        tree.insert(key)

    print("Árvore Splay:")
    tree.print_tree()

    search_key = 20
    if tree.search(search_key):
        print(f"A chave {search_key} está na árvore.")
    else:
        print(f"A chave {search_key} não está na árvore.")
