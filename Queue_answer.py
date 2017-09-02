
class Queue():
    def __init__(self, DefaultSize = 10, head = 0, tail = 0, count = 0):
        self.array = []
        self.DefaultSize = DefaultSize
        self.head = head
        self.tail = tail
        self.count = count
        def Enqueue(self, val):
            self.array.append(val)
             self.tail += 1
        def Dequeue(self):
            value = self.array[self.head]
            self.head += 1
            return value

        def Count(self):
            return self.tail - self.head
q = Queue()

q.Enqueue(5)
q.Enqueue(3)
q.Enqueue(13)
q.Enqueue(8)
q.Enqueue(2)
q.Enqueue(1)

q.Dequeue()

print(q.Count())
