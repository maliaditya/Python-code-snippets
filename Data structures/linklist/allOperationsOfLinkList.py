class Node:
    def __init__(self,data):
        self.data = data
        self.link = None


class LinkList:
    def __init__(self):
        self.start = None

    def  insertInList(self,newNode):
        if self.start == None:
            self.start = newNode
        else:
            lastNode = self.start
            while True:
                if lastNode.link == None:
                    break
                lastNode = lastNode.link
            lastNode.link = newNode

    def displayList(self):
        lastNode = self.start
        while True:
            if lastNode.link == None:
                print(lastNode.data)
                break
            print(lastNode.data)
            lastNode = lastNode.link

    def insertAtStart(self,newNode):
         newNode.link = self.start 
         self.start = newNode

    def deletAtEnd(self):
        lastNode = self.start
        while True:
            if lastNode.link == None:
                break
            secondLastNode = lastNode
            lastNode = lastNode.link
        secondLastNode.link = None

    def deleteAtStart(self):
        temp = self.start
        self.start = temp.link

    def insertAtSpecificPosition(self,newNode,position):
        node = self.start
        for a in range(position):
            prevNode = node
            node = node.link

        prevNode.link = newNode
        newNode.link = node

    def deleteAtSpecific(self,position):
        node = self.start
        for a in range(position):
            prevNode = node
            node = node.link

        prevNode.link = node.link



linklist = LinkList()

print("before insertion at start:")
print()

linklist.insertInList(Node("Python"))
linklist.insertInList(Node("Java"))
linklist.insertInList(Node("C"))
linklist.insertInList(Node("CPP"))
linklist.displayList()
print()
print("After insertion at start:")
print()
linklist.insertAtStart(Node("Javascript"))
linklist.displayList()

print()
print("After deletion at end:")
linklist.deletAtEnd()
print()
linklist.displayList()


print()
print("After deletion at start:")
linklist.deleteAtStart()
print()
linklist.displayList()


print()
print("After insertion at specific position no 2:")
linklist.insertAtSpecificPosition(Node("Ruby"),2) #python,java,ruby ,c
print()
linklist.displayList()


print()
print("After deletion at specific position no 1:")
linklist.deleteAtSpecific(1) #python,ruby ,c
print()
linklist.displayList()






