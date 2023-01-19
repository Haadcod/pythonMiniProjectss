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
        if self.headval is not None:
            self.headval.preval=newNode
        self.headval=newNode
    def listprint(self,node):
        while(node is not None):
            print(node.dataval)
            last=node
            node=node.nextval
dlist=DoublyLinkedList()
dlist.push(67)
dlist.push(24)
dlist.push(45)
dlist.push(78)
dlist.push(990)
dlist.listprint(dlist.headval)