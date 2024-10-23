class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_node(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)

        return root

def main():
    bst = BinarySearchTree()
    root = None
    root = bst.insert(root, 50)
    root = bst.insert(root, 30)
    root = bst.insert(root, 20)
    root = bst.insert(root, 40)
    root = bst.insert(root, 70)
    root = bst.insert(root, 60)
    root = bst.insert(root, 80)

    print("Inorder traversal: ", end="")
    bst.inorder(root)
    print()

    root = bst.delete_node(root, 20)
    print("After deletion of 20: ", end="")
    bst.inorder(root)
    print()

if __name__ == "__main__":
    main()
