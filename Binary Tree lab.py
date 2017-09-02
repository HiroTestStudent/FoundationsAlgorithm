
# Binary Tree lab

class Node():
    def __init__(self, data):
        # left node
        self.left = None
        # right node
        self.right = None
        # the node's data
        self.data = data

    def add(self, data):
        # if data exists
        if self.data:
            # check if the value is less than the current value
            if data < self.data:
                # if there is no data on the left, add it to the left
                if self.left is None:
                    self.left = Node(data)
                # otherwise recursively add to the left
                else:
                    self.left.add(data)
            # if data is larger, add it to the right
            pass

        # if there is no existing data, assign the value of input data to root
        else:
            self.data = data

    def printNodeInOrder(self):
        if self.data is not None:
            Node.printNodeInOrder(self.left)
            print(self.data + ",")
            Node.printNodeInOrder(self.right)


# initialize a node with a value of
root = Node(10)
root.add(20)
root.add(30)
print(root.printNodeInOrder)

