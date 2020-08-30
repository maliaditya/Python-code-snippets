
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
        if self.head is None:
            self.head = newNode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newNode
            newNode.prev = lastnode

    def display_list(self):
        lastnode = self.head
        while True:
            if lastnode.next is None:
                print(lastnode.data)
                break
            print(lastnode.data)
            lastnode = lastnode.next

    def display_reverse_list(self):
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

    def insert_At_Front(self,newNode):
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode


dll = DoublyLinkList()
dll.insert_at_end(Node("Aditya"))
dll.insert_at_end(Node("Aadesh"))
dll.insert_at_end(Node("Drumil"))
dll.insert_at_end(Node("Kundan"))
dll.display_list()
print()
print("Reversed List")
print()

dll.display_reverse_list()

print()
print("Add At Front")
print()
dll.insert_At_Front(Node("Shubham"))
dll.insert_At_Front(Node("Sujit"))
dll.display_list()
print()
print("Reversed List")
print()

dll.display_reverse_list()


        
    
        

