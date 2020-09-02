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
            rootNode.right = self.insertNode(rootNode.right, data)

        return rootNode



    def traversalInorder(self,root):
        if root is not None:
            self.traversalInorder(root.left)
            print(root.data)
            self.traversalInorder(root.right)




root = None
tree = Tree()
root =  tree.insertNode(root,1)
print(root.data)
tree.insertNode(root,2)
tree.insertNode(root,3)
tree.insertNode(root,4)
tree.insertNode(root,5)
tree.traversalInorder(root)

