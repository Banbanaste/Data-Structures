from collections import deque

"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "(node value: " + str(self.value) + " node left: %s node right: %s) " % (self.left, self.right)

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == value:
            return False
        node = BSTNode(value)
        if value < self.value:
            if self.left is None:
                self.left = node
            self.left.insert(value)
        if value > self.value:
            if self.right is None:
                self.right = node
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target is self.value:
            return True

        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)

        else:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each_preorder(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each_preorder(fn)
        if self.right:
            self.right.for_each_preorder(fn)
        return

    def for_each_inorder(self, fn):
        if self.left:
            self.left.for_each_inorder(fn)
        fn(self.value)
        if self.right:
            self.right.for_each_inorder(fn)
        return

    def for_each_postorder(self, fn):
        if self.left:
            self.left.for_each_postorder(fn)
        if self.right:
            self.right.for_each_postorder(fn)
        fn(self.value)
        return

    def breadth_first(self, fn):
        queue = deque()

        queue.append(self)

        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            fn(current.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):
        self.for_each_inorder(print)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        self.for_each_preorder(print)

    # Print Post-order recursive DFT
    def post_order_dft(self):
        self.for_each_postorder(print)


bst = BSTNode(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)

bst.pre_order_dft()
print("__" * 50)
bst.in_order_print()
print("__" * 50)
bst.post_order_dft()
print("__" * 50)
bst.breadth_first(print)
