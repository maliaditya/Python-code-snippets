
# Creating A Doubly Linked List Node  
class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
        self.prev = None


class DoublyLinkList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,newNode):
        self.head = newNode
        print(self.head.data)
        
        

#Creating object of Node Class

dll = DoublyLinkList()
dll.insert_at_end(Node("Aditya"))
