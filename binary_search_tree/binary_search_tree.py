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

    def insert(self, value):
    # Insert the given value into the tree
        # Left side
        if value < self.value:                  # If the value is on the left side is less than the root node
            if self.left is None:               # If it's empty, put it here
                self.left = BSTNode(value)      # Insert a node to this spot
            else:                               #
                self.left.insert(value)         # Recursive - calling itself

        elif value >= self.value:               # Right side
            if self.right is None:              # If there is no value to the right, insert it here by
                # assigning it to the right node.
                self.right = BSTNode(value)
            else:                               # If it doesn't go down that right side,
                self.right.insert(value)        # run it again.

    def contains(self, target):
    # Return True if the tree contains the value
    # False if it does not
        if self.value == target:                # If what we're looking for is the same as root
            return True

        if target < self.value:                 # If target is less than self.value
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        else:                                   # If target is greater than self.value
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


    def get_max(self):
    # Return the maximum value found in the tree
        # If there's only one node
        # Only deal with the right side as smaller values always go left
        current = self.right                    # Set the right node as the current node
        value = self.value                      # Set self.value to value
        while current != None:                  # If there's a node to the right,
            value = current.value               # update value to the current node &
            # set the node to the right as the current node.
            current = current.right
        return value


    def for_each(self, fn):
    # Call the function `fn` on the value of each node
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

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
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
