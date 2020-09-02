class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data


class Tree:

    def createNode(self,data):
        return Node(data)

    def insertNode(self,rootNode, data):
        if rootNode is None:
            return self.createNode(data)
        
        if data < rootNode.data:
            rootNode.left = self.insertNode(rootNode.left, data)
        elif data > rootNode.data:
            rootNode.right = self.insert(rootNode.right, data)

        return rootNode



            



root = None
tree = Tree()
root =  tree.insertNode(root,10)
print(root.data)