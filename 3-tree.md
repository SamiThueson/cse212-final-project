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

If the height of the left sub-tree and the right sub-tree are equal or differs at most by 1 level, the tree is known as balanced tree data structure.  

Balanced Binary Search Trees are O(log n).

**NOT FINISHED**

### Unbalanced

If the height of the left sub-tree and the right sub-tree differs by more than 1 level, then the tree is considered unbalanced. Unbalanced trees look like linked lists.

Unbalanced Binary Search Trees are O(n).

**NOT FINISHED**

## Operations

**NOT FINISHED**

## Example - Searching and Inserting Into a Tree

**NOT FINISHED**

```python
# A utility function to search a given key in BST
def search(root,key):
     
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
 
    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
   
    # Key is smaller than root's key
    return search(root.left,key)
```

```python
# A utility class that represents
# an individual node in a BST
 
 
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# A utility function to insert
# a new node with the given key
 

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
           root.left = insert(root.left, key)
    return root
 
# A utility function to do inorder tree traversal
 
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
 
```

## Problem to Solve

**NOT FINISHED**

[Back to Welcome Page](0-welcome.md)