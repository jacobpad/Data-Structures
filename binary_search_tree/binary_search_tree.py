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
###############################
########## CODE HERE ##########
###############################
from queue import Queue
from stack import Stack


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
        fn(self.value)
        if self.left:                           # If something to the left exists,
            self.left.for_each(fn)              # call it on the function
        if self.right:                          # If something to the right exists,
            self.right.for_each(fn)             # call it on the function

    # Part 2 -----------------------------------------------------------------
    # Part 2 -----------------------------------------------------------------
    # Part 2 -----------------------------------------------------------------
    # Part 2 -----------------------------------------------------------------

    # in_order_print ---------------------------------------------------------
    # in_order_print ---------------------------------------------------------
    # in_order_print ---------------------------------------------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        """
        # Print all the values in order from low to high
        # Hint:  Use a recursive, depth first traversal

        # What should we doif the current node is none?
        # Which direction should we move until we hit the end?
        # When should we switch the direction we're going?
        # If the current node is none, we know we've reached the end of a recursion.
        """

        if self is None:
            return
        # Check if we can move left
        if self.left is not None:
            self.left.in_order_print(self.left)
        # Visit the node by printing the value
        print(self.value)
        # Check if we can move right
        if self.right is not None:
            self.right.in_order_print(self.right)

    # bft_print --------------------------------------------------------------
    # bft_print --------------------------------------------------------------
    # bft_print --------------------------------------------------------------

    def bft_print(self, node):
        """
        # Print the value of every node, starting with the given node,
        # in an iterative breadth first traversal

        Import the queue class from the other day

        Use a queue to form a line for the nodes to get in

        - Place the root in the queue
        - Need a while loop
            - While length of the queue is greater than 0, 
              dequeue that item from the front and print it
        - Place current nodes left child (if not none) in the queue
        - Place current nodes right child (if not none) in the queue
        """

        # Instantiate the queue class
        q = Queue()

        # Put the root node in the queue
        q.enqueue(node)

        # While length of the queue is greater than 0
        while q.size > 0:

            #Instantiate
            dq = q.dequeue()

            # Print the dequeued value
            print(dq.value)

            # Try going left
            if dq.left:
                q.enqueue(dq.left)

            # Try going right
            if dq.right:
                q.enqueue(dq.right)

    # dft_print --------------------------------------------------------------
    # dft_print --------------------------------------------------------------
    # dft_print --------------------------------------------------------------

    def dft_print(self, node):
        """
        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal

        # Initialize an empty stack
        # Push the root node onto the stack
​
        # While loop to manager our iteration, if stack is not empty enter the while loop
            # Pop top item off the stack
            # Print that item's value
​
            # if there is a right subtree
                # push right item onto the stack
                
            # if there is a left subtree
                # push left item onto the stack
        """

        s = Stack()
        s.push(node)
        while s.size > 0:
            s_pop = s.pop()
            print(s_pop.value)

            if s_pop.right is not None:
                s.push(s_pop.right)
            if s_pop.left is not None:
                s.push(s_pop.left)

    # Stretch Goals ----------------------------------------------------------
    # Stretch Goals ----------------------------------------------------------
    # Stretch Goals ----------------------------------------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT

    def post_order_dft(self, node):
        pass
