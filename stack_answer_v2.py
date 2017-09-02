class Stack():

    def __init__(self):
        self.stack = []
        self.pointer = 0

    def Pop(self):
        if self.pointer > 0:
            #self.pointer -= 1
            self.pointer = self.pointer - 1
            self.stack.pop(self.pointer)
            print(self.pointer, self.stack)

    def Push(self, item):
        #self.pointer += 1
        self.pointer = self.pointer + 1
        self.stack.append(item)
        print(self.pointer, self.stack)

    def Top(self):
        if self.pointer > 0:
            return self.stack[self.pointer - 1]
        else:
            return 'stack is empty'

    def isEmpty(self):
        return self.pointer == 0

    def Size(self):
        return self.pointer

#main

stack = Stack()

print(stack.Top())

print(stack.isEmpty())
print(stack.Size())

stack.Push(1)
print(stack.isEmpty())
stack.Push(10)
stack.Push(8)
stack.Pop()
stack.Push(20)
print(stack.Top())
stack.Push(18)

while not stack.isEmpty():
    stack.Pop()

print(stack.isEmpty())

print(stack.Top())
