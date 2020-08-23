class Node:
    def __init__(self,data):
        self.data = data
        self.link = None

class LinkList:
    def __init__(self):
        self.start = None

    def insert(self,newNode):
        if self.start == None:
            self.start = newNode
        else:
            lastNode = self.start
            while True:
                if lastNode.link is None:
                    break
                lastNode = lastNode.link
            lastNode.link = newNode  

    def displayList(self):
        lastnode = self.start
        while True:
            if lastnode.link is None:
                print(lastnode.data)
                break
            print(lastnode.data)
            lastnode = lastnode.link

    def insertAtStart(self,newNode):
        newNode.link = self.start
        self.start=newNode
        
       

        
              
linkList = LinkList()

linkList.insert(Node("Manu"))
linkList.insert(Node("Pratu"))
linkList.insert(Node("Guddi"))
linkList.insert(Node("Megha"))
linkList.insert(Node("Shital"))


print()
print("Before insertion")
linkList.displayList()
print()

linkList.insertAtStart(Node("Aditya"))

print("After insertion")

print()
linkList.displayList()

    


