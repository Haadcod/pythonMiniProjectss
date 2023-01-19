class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class Linkedlist:
    def __init__(self):
        self.headval=None
    def list_print(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
list=Linkedlist()
list.headval=Node('mon')
e2=Node('wed')
e3=Node('tue')
e4=Node('fri')
e5=Node('sun')
e6=Node('sat')
e7=Node('thu')
list.headval.nextval=e3
e3.nextval=e2
e2.nextval=e7
e7.nextval=e4
e4.nextval=e6
e6.nextval=e5
list.list_print()

