class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,newNode):
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
        else:
            lastnode = self.head
            while True:
                if lastnode.next is self.head:
                    break
                lastnode = lastnode.next
            lastnode.next = newNode
            newNode.next = self.head


    def displayLinkedList(self):
        lastnode = self.head
        while True:
            if lastnode.next is self.head:
                print(lastnode.data)
                break
            print(lastnode.data)
            lastnode = lastnode.next



scll = SinglyCircularLinkedList()
scll.insert_at_end(Node("Aditya"))
scll.insert_at_end(Node("Manu"))
scll.insert_at_end(Node("Pratu"))

scll.displayLinkedList()

    
            

        