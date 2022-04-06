Trees are very similar and almost identical to linked lists. They are made up of nodes that are connected to one another. But unlike linked lists, they are connected in a "tree" like form. Tree's can have more than one node connected to each other.

## What Makes Up a Tree

At the basic level a tree consists of the root, parent, and child.

The topmost node of a tree or the node which does not have any parent node is called the **root** node. Connected to the root node are **parent** nodes, but what truly makes a parent node is the fact the it has **child** nodes.

Other worthy mentions are leaf nodes and subtrees. The nodes which do not have any child nodes are called **leaf** nodes. And a **subtree** is any node of the tree along with its descendant.

## General Tree

A general tree data structure has no restriction on the number of nodes. It means that a parent node can have any number of child nodes.  

## Binary Tree

A node of a binary tree can have a maximum number of two child nodes.

## Binary Search Tree

In a binary search tree each node is greater than every node in it's left subtree, and each node is less than every node in it's right subtree. 

In simpler terms every node to the left of the root node is less than the root node and every node to the right of the root node is greater.

As the name implies, binary search trees are used for various searching and sorting algorithms. The examples include AVL tree and red-black tree. It is a non-linear data structure.

![Binary Search Tree](binary_tree.jpg)

### Balanced

If the height of the left sub-tree and the right sub-tree are equal or differs at most by 1 level, the tree is known as a balanced tree data structure.  

Balanced Binary Search Trees are O(log n) because they essentially start in the middle of the tree and, depending on what node you are looking for, will either start search to the right or left of the root node.

### Unbalanced

If the height of the left sub-tree and the right sub-tree differs by more than 1 level, then the tree is considered unbalanced. Unbalanced trees look like linked lists.

Unbalanced Binary Search Trees are O(n) because they have to start their search from the beginning of the tree to, worst case senario, the end.

## Operations

There is not exact functions that you can use for binary search trees because python doesn't have a built-in BST class, but there are common functions that are used. 

As a side note, there are packages from other developers that implement BST functions. Bintrees is an example of one of those packages.

Operation | Purpose | Big O
-------- | -------- | --------
Search/Traverse | Visits all objects in the tree | O(n) Goes through both the left and the right sub-trees
Insert | Inserts a value into the tree | O(log n) Only goes through sub-trees that are necessary to find it's place 
Delete | Removes a value from the tree | O(log n) Only goes through sub-trees that are necessary to find the value


## Example - Searching and Inserting Into a Tree

Something we have yet to talk about which is essential to trees is recursion. Just about every operation for a tree uses recursion.

When you search a binary tree you are traversing it. An inorder traversal visits the nodes from smallest to largest, and you can also visit them from largest to smallest in a reverse traversal.

Traversing uses the recursive process. When using recursion you must come up with the smaller problem to solve and the base case. The smaller problem for traversing a binary search tree then is to traverse the left sub-tree, use the current node, and traverse the right sub-tree. The base case is to not recursively traverse a sub-tree if it is empty. 

One way of traversing inorder is shown below.

```python
# Inorder traversal
def inorder(root):
    if root is not None:
        # Traverse left
        inorder(root.left)

        # Traverse root
        print(str(root.key) + ", ", end=' ')

        # Traverse right
        inorder(root.right)
```
Inserting into a binary search tree also uses recursion. The smaller problem for inserting into a binary search tree is whether you insert the value into the left sub-tree or right sub-tree based on what the value. The base case for inserting into a binary search tree is whether the sub-tree is empty or not, meaning the correct place has been found because there's space for a node to be inserted.

Shown below is an example of how a node can be inserted into a BST.

```python
# Create a node class.
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
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
```

## Problem to Solve

For this problem you will need to create a BST of your own. In this BST you will perform various functions to insert, traverse forwards, and traverse backwards.

First create your BST and create an insert function. After you have accomplished this, create a fuction that will traverse the BST forwards and create another function that with traverse the BST backwards.

Once you have finished, insert up to 10 numbers into the BST. Use your other functions to show that you can traverse forwards and backwards.

Your output should look something like this.
```
Forward Traverse:
1, 3, 4, 6, 7, 8, 10, 11

Backward Traverse:
11, 10, 8, 7, 6, 4, 3, 1
```

You can check your code with the solution here: [Solution](tree-solution.py)

[Back to Welcome Page](0-welcome.md)