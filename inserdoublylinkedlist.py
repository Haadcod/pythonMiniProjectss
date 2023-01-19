class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
        self.preval=None
class DoublyLinkedList:
    def __init__(self):
        self.headval=None
    def push(self,newval):
        newNode=Node(newval)
        newNode.nextval=self.headval
        if (self.headval is not None):
            self.headval.preval =newNode
        self.headval=newNode
    def insert(self,prev_node,newval):
        if prev_node is not None:
            return
        newNode=Node(newval)
        prev_node.nextval=newNode
        newNode.preval=prev_node
        if newNode.nextval is not None:
            newNode.nextval.preval=newNode
    def printlist(self,node):
        while(node is not None):
            print(node.dataval)
            last =node
            node=node.nextval
dlist=DoublyLinkedList()
dlist.push(239)
dlist.push(80)
dlist.push(90)
dlist.push(12)
dlist.push(60)
dlist.insert(dlist.headval.nextval,13)
dlist.printlist(dlist.headval)

