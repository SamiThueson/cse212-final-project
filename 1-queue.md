The queue is a linear data structure used to represent a linear list. Unlike a stack, which is Last In First Out (LIFO), a queue stores items in a First In First Out (FIFO) manner. And like a stack, it can be implemented using a python list.

## What is a Queue

A queue is a linear list of elements in which deletion of an element can take place only at one end called the ***front*** and insertion can take place on the other end which is termed as the ***rear***.

In a queue, the first element that is inserted will also be the first one removed. That is why it's called First In First Out. 

An example of how a queue works would be a line of people waiting to order food. The first person in line orders their food and exits the line. Someone who just got to the resturant and wants to order food enters the line at the rear. This way of organization keeps everyone in there right place, so that whoever got in line first gets to order first. 

There are a couple more technical terms we use for queues. ***Enqueue*** adds an item to the back of the queue. While ***dequeue*** removes and item from the front of the queue. 

## Big O of Queues

We will talk about two different ways we can implement a queue. 

You can use a list to implement a queue in python. You use append() and pop(), instead of enqueue() and dequeue(). Though using a list to implement a queue is a lot slower because each time you insert or remove an element, all the elements have to be shifted by one. This results in O(n) time.

Using the deque class from the collections module is preferred over using lists when quicker operations are needed. Deque still uses append and pop operations, but they result in O(1) time versus a lists O(n) time. Instead of enqueue() and dequeue(), deque uses append() and popleft() functions.

## Operation

When using a list or using the deque class the operations do the same thing. The only difference is whether they use pop() or popleft().

Operation | Purpose | List or Deque
-------- | -------- | -------- 
queue.append(data) | Adds data to end of queue | Both
queue.pop(0) | Removes element from front of queue | List
queue.popleft() | Removes element from front of queue | Deque
length = len(queue) | Returns length of queue | Both
len(queue) == 0 | Checks if the queue is empty | Both


## Example - Using a List and Deque

Using a list is very straight forward and easy to understand. You implement the queue with a list and use append and pop just like you would with any other list.

```python
# Initialize a queue.
queue = []

# Add elements to the queue.
queue.append("h")
queue.append("e")
queue.append("l")
queue.append("l")
queue.append("o")

print(f"Queue: {queue}")

# Remove elements from the queue.
print("\n Elements removed from queue.")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\n The rest of the queue.")
print(queue)
```

The deque class is also just as easy to use as a list. You intialize the queue with the deque method and use it like you would a list, but with append and popleft. 

```python
from collections import deque

# Initialize a queue.
queue = deque()

# Add elements to the queue.
queue.append("w")
queue.append("o")
queue.append("r")
queue.append("l")
queue.append("d")

print(f"Queue: {queue}")

# Remove elements from the queue.
print("\n Elements removed from queue.")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print("\n The rest of the queue.")
print(queue)
```

## Problem to Solve

For this problem you are going to reverse the order of a certain amount of elements in a queue.

The user will provide a number and the program will then reverse the n amount of elements order in the queue, leaving the other elements relatively untouched. 

For example the user could give the number 5, the order of the first 5 elements of the queue would then need to be reversed, but the rest of the queue is left untouched. 

An approach to solve this problem could be to use another data structure to store the first n amount of elements in and then re-insert into the original queue. 

But whatever approach you decide to use, your output should look something like this.

```
How many of the first n elements of the queue would you like to reverse? Please provide a number:
> 5

5 elements were reversed in the queue:
50 40 30 20 10 60 70 80 90 100
```

You can check your code with the solution here: [Solution](queue-solution.py)

[Back to Welcome Page](0-welcome.md)