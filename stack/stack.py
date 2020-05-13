"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# stack w/ array
""" 
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if not self.__len__():
            return None
        return self.storage.pop()
 """

# stack w/ linked list


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


class Stack:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, data):
        node = Node(data, self.root)
        self.root = node
        self.size += 1
        print(node)

    def pop(self):
        currenthead = self.root
        if currenthead:
            newhead = currenthead.get_next()
            self.root = newhead
            self.size -= 1
            return currenthead.data
        return None

    def find(self, data):
        current = self.root
        while current:
            if current.get_data() == data:
                return data
            else:
                current = current.get_next()
        return None
