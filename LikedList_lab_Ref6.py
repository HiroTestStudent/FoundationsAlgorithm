'''Data structures implemented with linked lists.'''


class Node:

    def __init__(self, value):
        self.value = value
        self.next_node = None


class Stack():

    def __init__(self, value):
        self.head = None
        self.value = value
        self.next_node = None

    def push(self, item):

        temp = Node(item)
        temp.next_node = self.head
        self.head = temp

    def pop(self):

        if self.isEmpty():
            raise IndexError("Can\'t pop from empty stack.")
        else:
            temp = self.head.data
            self.head = self.head.next_node
            return temp

            # use the following if stack is empty
            # raise IndexError("Can't pop from empty stack.")

    def peek(self):
        """pop an item on the top of the top of the stack, but don't remove it"""

        return self.head.data

    def isEmpty(self):
        return self.head == None


