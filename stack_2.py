class Stack:
    def __init__(self):
        self.stack = []

    def Pop(self, item):
        return self.stack.pop(item)

    def Top(self):
        return self.stack[-1]

    def isEmpty(self):
        return self.stack == []

    def Push(self, item):
        self.stack.append(item)

    def Size(self):
        return len(self.stack)


stack = Stack()
stack.Push(5)
stack.Push(3)
stack.Push(2)
stack.Push(9)
stack.Pop(9)
stack.Pop(2)
stack.Pop(3)
stack.Pop(5)

print("The last value pushed was {}.".format(stack.Top()))


#while not stack.isEmpty():
    #print("Popping {}".format(stack.Pop()))