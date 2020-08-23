import time

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



class Switch:
    def __init__(self,case):
        self.case = getattr(self,"case_"+ case,"Wrong Choice")()
        
    
    def case_1(self):
        return linklist.insertInList(Node(input("-> Enter the data to be inserted: ")))
        
    def case_2(self):
        return linklist.insertAtStart(Node(input("-> Enter the data to be inserted: ")))
        
    def case_3(self):
        return linklist.insertAtSpecificPosition(Node(input("-> Enter the data to be inserted: ")),int(input("-> Enter the location for the data to be inserted: ")) )

    def case_4(self):
        return linklist.deletAtEnd()

    def case_5(self):
        return linklist.deleteAtStart()

    def case_6(self):
        return linklist.deleteAtSpecific(int(input("-> Enter the location for the data to be inserted: ")))

    def case_7(self):
        return linklist.displayList()
        



n = 0
while n != 8:
    print()
    print("1. Insert at end.")
    print("2. Insert at start.")
    print("3. Insert at specific location.")
    print("4. Delete at end.")
    print("5. Delete at start.")
    print("6. Delete at specific location.")
    print("7. Display List.")
    print("8. Exit.")
    print()

    a = input("-> Enter your choice: ")

    print()

    if int(a) == 8:
        print("**** Thankyou ****")
        break
    elif int(a) >=8:
        print("###### Wrong Choice #######")
        time.sleep(0.5)
        continue
    else:
        Switch(a)





