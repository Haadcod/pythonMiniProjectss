class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.preval=None
        self.nextval=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def push(self,newval):
        newnode= Node(newval)
        newnode.nextval=self.head
        if self.head is not None:
            self.head.prev=newnode
        self.head=newnode
    def printlist(self,node):
        while(node is not None):
            print(node.dataval),
            last=node
            node=node.nextval
dlist=DoublyLinkedList()
dlist.push(13)
dlist.push(34)
dlist.push(90)
dlist.push(34)
dlist.push(12)
dlist.printlist(dlist.head)
