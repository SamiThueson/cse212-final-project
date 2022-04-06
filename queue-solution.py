from queue import Queue
 
# Function to reverse the first n
# elements of the Queue.
def reverseNQueue(n, Queue):
    if (Queue.empty() == True or n > Queue.qsize()):
        return
    if (n <= 0):
        return
 
    Stack = []
 
    # Put the first n elements
    # into a Stack.
    for i in range(n):
        Stack.append(Queue.queue[0])
        Queue.get()

    # Enqueue the contents of the stack
    # at the back of the queue.
    while (len(Stack) != 0 ):
        Queue.put(Stack[-1])
        Stack.pop()
 
    # Remove the remaining elements and
    # enqueue them at the end of the Queue.
    for i in range(Queue.qsize() - n):
        Queue.put(Queue.queue[0])
        Queue.get()
 
# Utility Function to print the Queue.
def Print(Queue):
    while (not Queue.empty()):
        print(Queue.queue[0], end =" ")
        Queue.get()

# Driver code.
if __name__ == '__main__':
    Queue = Queue()
    Queue.put(10)
    Queue.put(20)
    Queue.put(30)
    Queue.put(40)
    Queue.put(50)
    Queue.put(60)
    Queue.put(70)
    Queue.put(80)
    Queue.put(90)
    Queue.put(100)
    
    n = int(input("How many of the first n elements of the queue would you like to reverse? Please provide a number: "))

    print()
    print(f"{n} elements were reversed in the queue:")
    reverseNQueue(n, Queue)
    Print(Queue)
    print()
