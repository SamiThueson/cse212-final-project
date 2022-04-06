class LinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None

        def __repr__(self):
            return self.data

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        #nodes.append("None")
        return ", ".join(nodes)

    def __iter__(self):
        # Start at the head and go through each node in the list until you hit None.
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_head(self, node):
        # Create a new node.
        n_node = LinkedList.Node(node)
        # If the list is empty, then assign the node as both the head and tail.
        if self.head is None:
            self.head = n_node
            self.tail = n_node
        # Otherwise insert the new node at the head. 
        else:
            n_node.next = self.head
            self.head.prev = n_node
            self.head = n_node

    def add_tail(self, node):
        # Create a new node.
        n_node = LinkedList.Node(node)
        # If the list is empty, then assign the node as both the head and tail.
        if self.tail is None:
            self.head = n_node
            self.tail = n_node
        # Otherwise insert the new node at the tail. 
        else:
            n_node.prev = self.tail
            self.tail.next = n_node
            self.tail = n_node

    def remove_head(self):
        # If there is one item in the list set it to be None.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If there is more than one item in the list, only the head will be affected.
        elif self.head is not None:
            self.head.next.prev = None
            self.head = self.head.next

    def remove_tail(self):
        # If there is one item in the list set it to be None.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If there is more than one item in the list, only the tail will be affected.
        elif self.tail is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev

llist = LinkedList()

llist.add_tail(input("Please provide what song you would like to add: "))
llist.add_tail(input("Please provide what song you would like to add: "))
llist.add_tail(input("Please provide what song you would like to add: "))
llist.add_tail(input("Please provide what song you would like to add: "))
llist.add_tail(input("Please provide what song you would like to add: "))
print()
#print(llist)
for node in llist:
    print(node)
print()

print("Remove the first and last song from the list: ")
llist.remove_head()
llist.remove_tail()
print(llist)
print()

llist.add_head(input("Insert a new song at the head: "))
llist.add_tail(input("Insert a new song at the tail: "))
print()
#print(llist)
for node in llist:
    print(node)
print()
