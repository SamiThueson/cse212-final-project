# Create a node class.
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Forward traversal.
def forward_traverse(root):
    if root is not None:
        # Traverse left.
        forward_traverse(root.left)

        # Traverse root.
        print(str(root.key) + ", ", end=' ')

        # Traverse right.
        forward_traverse(root.right)

# Backward traversal.
def backward_traverse(root):
    if root is not None:
        # Traverse right.
        backward_traverse(root.right)

        # Traverse root.
        print(str(root.key) + ", ", end=' ')

        # Traverse left.
        backward_traverse(root.left)

# Insert a node.
def insert(node, key):

    # Return a new node if the tree is empty.
    if node is None:
        return Node(key)

    # Traverse to the right place and insert the node.
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 11)
root = insert(root, 4)

print("Forward Traverse: ", end=' ')
forward_traverse(root)
print()

print("Backward Traverse: ", end=' ')
backward_traverse(root)
print()
