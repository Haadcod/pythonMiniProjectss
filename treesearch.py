class Node:
    def __init__(self,dataval):
        self.right=None
        self.left=None
        self.dataval=dataval
    def printTree(self):
        print(self.dataval)
root=Node(10)
root.printTree()