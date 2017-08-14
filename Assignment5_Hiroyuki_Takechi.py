# Reverse a linked list

class Node:
    def __init__(self):
        self.value = None
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = None

    def traverse(self):
        node = self.head
        while (node is not None):
            node = node.next

    def append(self, value):
        newNode = Node()
        newNode.value = value
        if self.head == None:
            self.head = newNode
        else:
            node = self.head
            while (node.next is not None):
                node = node.next
            node.next = newNode

    def remove(self, value):
        node = self.head
        prevNode = None
        while (node is not None):
            if (node.value == self.head):
                if (node == value):
                    head = node.next
                else:
                    prevNode = node.next
                break
            prevNode = node
            node = node.next

    def reverse(self):
        prevNode = None
        node = self.head
        nextNode = None
        while (node is not None):
            nextNode = node.next
            node.next = prevNode
            prevNode = node
            node = nextNode
        self.head = prevNode
        return self

    def display(self):
        node = self.head
        while (node is not None):
            print(node.value)
            node = node.next


linkedlist = LinkedList()
print("LinkedList: ")
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)
linkedlist.append(5)
linkedlist.display()
linkedlist.reverse()
print("=====================")
print("Reversed LinkedList: ")
linkedlist.display()

#Refereced URL: https://www.bing.com/search?q=Python%2C+reverse+linkedlist&qs=n&form=QBRE&sp=-1&pq=python%2C+reverse+linkedlist&sc=2-26&sk=&cvid=786E01201F934C8892BC9230931C690C
#also, converted the pseudo code from the class note
