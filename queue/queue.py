"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):
        self.size -= 1
        if not self.__len__():
            return None
        return self.storage.pop(0)
 """


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class Queue:
    def __init__(self):
        self.size = 0
        self.root = None
        self.end = None

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        node = Node(value)
        if not self.root and not self.end:
            self.root = node
            self.end = node
        else:
            self.end.set_next(node)
            self.end = node

    def dequeue(self):
        if not self.root:
            return None
        else:
            self.size -= 1
            dequeuedata = self.root.get_data()
            self.root = self.root.get_next()
            return dequeuedata
