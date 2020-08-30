class Node:
    def __init__(self,data):
        self.prev = None
        self.data =  data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            prevNode = self.head
            while True:
                if lastNode.next is None:
                    break
                prevNode = lastNode
                lastNode = lastNode.next  
            lastNode.next = newNode
            if prevNode is self.head:
                prevNode.prev = None
            newNode.prev = prevNode
            

    def displayLinkList(self):
        lastnode = self.head
        while True:
            if lastnode.next is None:
                print(lastnode.data)
                break
            print(lastnode.data)
            lastnode = lastnode.next

    def displayRevesered(self):
        lastnode = self.head
        while True:
            if lastnode.next is None:
                break
            lastnode = lastnode.next
        while True:
            if lastnode.prev is None:
                print(lastnode.data)    
                break
            print(lastnode.data)
            lastnode = lastnode.prev

        
       
        

    
newNode = Node('Aditya')
dll = DoublyLinkedList()
dll.insertAtEnd(newNode)
newNode = Node('Aadesh')
dll.insertAtEnd(newNode)

newNode = Node('Drumil')
dll.insertAtEnd(newNode)

newNode = Node('Kundan')
dll.insertAtEnd(newNode)

dll.displayLinkList()
dll.displayRevesered()