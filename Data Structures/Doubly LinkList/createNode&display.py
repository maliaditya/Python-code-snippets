
# Creating A Doubly Linked List Node  
class Node:
    def __init__(self, next=None, data = None, prev = None):
        self.next = next
        self.data = data
        self.prev = prev


#Creating object of Node Class

newNode = Node(data = "Aditya")
print(newNode.data)
