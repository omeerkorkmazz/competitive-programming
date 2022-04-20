class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class MyQueue:

    def __init__(self):
        self.queue = None
        self.iterator = None

    # Function to push an element into the queue.
    def push(self, item):
        if self.queue == None:
            self.queue = Node(item)
            self.iterator = self.queue
        else:
            self.iterator.next = Node(item)
            self.iterator = self.iterator.next

    # Function to pop front element from the queue.
    def pop(self):
        val = -1
        if self.queue != None:
            val = self.queue.data
            self.queue = self.queue.next
        return val
