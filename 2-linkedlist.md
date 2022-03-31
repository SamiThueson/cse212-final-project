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

**NOT FINISHED**

## Problem to Solve

For this problem you are going to create a music player using a doubly linked list. 

Start by creating a linked list without using the deque module. You will then add 10 of your favorite songs to the list. 

Next you will need to remove 1 song from the head, tail, and somewhere in the middle. 

Afterwards you will insert those songs back into the linked list where they were originally removed from.

Your output should look something like this.
```python
Please provide what song you would like to add: 


```

**NOT FINISHED**

[Back to Welcome Page](0-welcome.md)