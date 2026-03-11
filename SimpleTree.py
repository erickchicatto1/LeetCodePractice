class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None


    # Insert
    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right


    # Search
    def search(self, value):

        current = self.root

        while current:

            if value == current.value:
                return True

            elif value < current.value:
                current = current.left

            else:
                current = current.right

        return False


    # Inorder Traversal
    def inorder(self, node):

        if node:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)


    # Preorder Traversal
    def preorder(self, node):

        if node:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)


    # Postorder Traversal
    def postorder(self, node):

        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)
