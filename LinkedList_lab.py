
# Linked List lab


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():

    count = 0

    def __init__(self, value):
        self.value = value
        self.Next = None
        self.head = None

    def Push(self, item):
        p = Node(item)
        p.next = self.head
        self.head = p
        count += 1

    def pop(self):
        count -+ 1
        head = self.head
        self.head = head.next
        return head

    def Top(self):
        return self.head

    def isEmpty(self):
        return self.head == None

    def Main():

        stack = Stack()
        stack.Push(5)
        stack.Push(3)
        stack.Push(2)
        stack.Push(9)

        print("The last value pushed was {}".format(stack.Top()))

        while stack.IsEmpty() == "False":
            print("Popping {}".format(stack.Pop()))


print(Stack.Main())

