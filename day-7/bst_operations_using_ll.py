# Node structure for the BST
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to insert a node in the BST
def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    
    return root

# Inorder traversal of BST (Left, Root, Right)
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Preorder traversal of BST (Root, Left, Right)
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Postorder traversal of BST (Left, Right, Root)
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

# Function to find the minimum value node
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Delete a node from the BST
def deleteNode(root, key):
    if root is None:
        return root

    # Traverse to the correct node
    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        # Node with one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # Node with two children: Get the inorder successor
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)

    return root

# Search for a node in the BST
def search(root, key):
    if root is None or root.data == key:
        return root

    if key < root.data:
        return search(root.left, key)

    return search(root.right, key)

# Main function to demonstrate the BST operations
if __name__ == "__main__":
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    print("Inorder traversal: ", end="")
    inorder(root)
    print()

    print("Preorder traversal: ", end="")
    preorder(root)
    print()

    print("Postorder traversal: ", end="")
    postorder(root)
    print()

    print("\nDeleting 20")
    root = deleteNode(root, 20)
    print("Inorder traversal after deletion: ", end="")
    inorder(root)
    print()

    print("\nSearching for 40: ", end="")
    foundNode = search(root, 40)
    if foundNode is not None:
        print("Found")
    else:
        print("Not Found")
