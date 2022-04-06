A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers.
In simple words, a linked list consists of nodes where each node contains a data field and a link to the next node in the list.

## What Makes Up a Linked List

Linked lists are made up of **nodes** and **pointers**. The first node in a linked list is called the **head** and the last node is called a **tail**. If there is only one node in a linked list then that node is reffered to as both the head and tail.

The node in a linked list is the equavilent to an element in an array. It holds a value. 

A pointer references to a node. A **next** pointer points to the next node in the list, and a **previous** pointer points to the previous node. 

### Singly Linked List

A singly linked list consists of  nodes that have next pointers. You can traverse forward through a singly linked list, but not backwards.

### Doubly Linked List

Doubly linked list are bi-directional and consit of nodes that have both next pointers and previous pointers. You can traverse forwards and backwards through a doubly linked list. This is the most common kind of linked list you will see. 

## Big O of Linked Lists

When inserting or removing the head or tail from a linked list the performance is O(1). This is why linked list have an advantage over normal lists when implementing queues, which are first in first out. 

However when it comes to looking up an element in the middle of a linked list the performance becomes O(n). This is because you have to traverse the list until you find the element you were looking for.

## Operations

In python the collections module has a specific object called deque() that you can use for linked lists. It has the following operations.

Operation | Purpose 
-------- | -------- 
linkL = deque("abcde") | Creates a linked list
linkL.append("f") | Adds element to end of list
linkL.pop() | Removes element from end of list
linkL.appendleft("g") | Adds element to front of list
linkL.popleft() | Removes element from front of list
linkL.insert("c", "h") | Adds "h" after node "c"
linkL.remove("c") | Remove node "c"
length = len(linkL) | Returns the size of the list


## Example - How to Create Your Own

You can also just create your own linked lists by creating classes for a linked list and node.

In this example we will be creating a bi-directional linked list. Please follow along closely as this example will help you solve the problem.

To create your own linked list we first need to create a linked list class and give the attributes for the head and tail.

```python
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
```
Next we will create a node class with the attributes data, next, and previous pointers.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
```

From here you can create different functions within the classes that can insert, remove, traverse the linked list, and many more. 

To insert into the head of a linked list you just need to identify if the list is empty and insert your new node at the head. It's pretty easy to insert at the head of a linked list.

```python
def add_head(self, node):
    # If the list is empty, then assign the node as both the head and tail.
    if self.head is None:
        self.head = node
        self.tail = node
    # Otherwise insert the new node at the head. 
    else:
        node.next = self.head
        self.head.prev = node
        self.head = node
```

Traversing a linked list is just a fancier way of saying iterating a list. We can use __iter__ to add a behavior to the linked list that you would expect from a normal list. (Yielding stops at every node in the list.)

```python
def __iter__(self):
    # Start at the head and go through each node in the list until you hit None.
    node = self.head
    while node is not None:
        yield node
        node = node.next
```

Removing the tail of a linked list is pretty straight forward. It's similar to inserting at the head of a linked list. You first check if the list has any items in it, and if it has more than one item then only the tail will be affected.

```python
def remove_tail(self):
    # If there is one item in the list set it to be None.
    if self.head == self.tail:
        self.head = None
        self.tail = None
    # If there is more than one item in the list, only the tail will be affected.
    elif self.tail is not None:
        self.tail.prev.next = None
        self.tail = self.tail.prev
```

## Problem to Solve

For this problem you are going to create a music player using a doubly linked list. 

Start by creating a linked list without using the deque module. You will then add 5 of your favorite songs to the list. 

Next you will need to remove 1 song from the head and 1 from the tail. 

Afterwards you will insert two new songs back into the linked list at the head and tail.

Your output should look something like this.

```
Please provide what song you would like to add: 
> Dont Stop Me Now

Please provide what song you would like to add: 
> Lost In Japan

Please provide what song you would like to add: 
> Sunday Best

Please provide what song you would like to add: 
> idontwannabeyouanymore

Please provide what song you would like to add: 
> Ophelia

Dont Stop Me Now
Lost In Japan
Sunday Best
idontwannabeyouanymore
Ophelia

Remove the first and last song from the list:
Lost In Japan, Sunday Best, idontwannabeyouanymore

Insert a new song at the head:
> Superlove

Insert a new song at the tail:
> One Man Band

Superlove
Lost In Japan
Sunday Best
idontwannabeyouanymore
One Man Band
```
You can check your code with the solution here: [Solution](linkedlist-solution.py)

[Back to Welcome Page](0-welcome.md)