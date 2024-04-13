class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotateRight(self, y):
        x = y.left
        T = x.right

        x.right = y
        y.left = T

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x

    def rotateLeft(self, x):
        y = x.right
        T = y.left

        y.left = x
        x.right = T

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def insert(self, node, key):
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        balance = self.getBalance(node)

        if balance > 1:
            if key < node.left.key:
                return self.rotateRight(node)
            else:
                node.left = self.rotateLeft(node.left)
                return self.rotateRight(node)

        if balance < -1:
            if key > node.right.key:
                return self.rotateLeft(node)
            else:
                node.right = self.rotateRight(node.right)
                return self.rotateLeft(node)

        return node

    def preOrder(self, node):
        result = []
        if not node:
            return result
        result.append(node.key)
        result += self.preOrder(node.left)
        result += self.preOrder(node.right)
        return result


def main():
    myTree = AVLTree()
    root = None
    
    root = myTree.insert(root, 10)
    root = myTree.insert(root, 20)
    root = myTree.insert(root, 30)
    root = myTree.insert(root, 40)
    root = myTree.insert(root, 50)
    root = myTree.insert(root, 25)
    
    print("AVL Tree in pre order")
    result = myTree.preOrder(root)
    print(result)
    
    
if __name__ == "__main__":
    main()
