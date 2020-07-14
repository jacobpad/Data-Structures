from singly_linked_list import Node, LinkedList


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
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         return self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) == 0:
#             return None
#         return self.storage.pop(0)
        

# class Node:
#     def __init__(self, value=None, next_node=None):
#         # the value at this linked list node
#         self.value = value
#         # reference to the next node in the list
#         self.next_node = next_node

#     def get_value(self):
#         return self.value

#     def get_next(self):
#         return self.next_node

#     def set_next(self, new_next):
#         # set this node's next_node reference to the passed in node
#         self.next_node = new_next



class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList() #using LL (LinkedLists)

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()
