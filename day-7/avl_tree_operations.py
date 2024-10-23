# AVL Tree Node structure
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Function to get the height of the tree
def height(node):
    if not node:
        return 0
    return node.height

# Function to right rotate subtree rooted with y
def rightRotate(y):
    x = y.left
    T2 = x.right

    # Perform rotation
    x.right = y
    y.left = T2

    # Update heights
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x

# Function to left rotate subtree rooted with x
def leftRotate(x):
    y = x.right
    T2 = y.left

    # Perform rotation
    y.left = x
    x.right = T2

    # Update heights
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y

# Get the balance factor of node N
def getBalance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

# Recursive function to insert a key in the subtree rooted
# with node and returns the new root of the subtree.
def insert(node, key):
    # Perform normal BST insertion
    if not node:
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node

    # Update the height of the current node
    node.height = 1 + max(height(node.left), height(node.right))

    # Get the balance factor of this node to check whether
    # it became unbalanced
    balance = getBalance(node)

    # If this node becomes unbalanced, then there are 4 cases

    # Left Left Case
    if balance > 1 and key < node.left.key:
        return rightRotate(node)

    # Right Right Case
    if balance < -1 and key > node.right.key:
        return leftRotate(node)

    # Left Right Case
    if balance > 1 and key > node.left.key:
        node.left = leftRotate(node.left)
        return rightRotate(node)

    # Right Left Case
    if balance < -1 and key < node.right.key:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node

# Function to print the inorder traversal of the tree
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Driver code to test the AVL tree
if __name__ == "__main__":
    root = None

    # Inserting nodes into the AVL tree
    root = insert(root, 10)
    root = insert(root, 20)
    root = insert(root, 30)
    root = insert(root, 40)
    root = insert(root, 50)
    root = insert(root, 25)

    # Printing the inorder traversal of the tree
    print("Inorder traversal of the constructed AVL tree is:")
    inorder(root)
