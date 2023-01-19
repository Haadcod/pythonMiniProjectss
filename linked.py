class Node:
    def __init__(self,value,next_node=None):
        self.value=value
        self.next_node=next_node
    def set_next_node(self,next_node):
        self.next_node=next_node
    def get_next_node(self,next_node):
        return self.next_node
    def get_value(self,value):
        return self.value
e1=Node('mon')
e2=Node('wed')
e3=Node('tue')
e4=Node('fri')
e5=Node('sun')
e6=Node('sat')
e7=Node('thu')
e1.next_node=e3
e3.next_node=e2
e2.next_node=e7
e7.next_node=e4
e4.next_node=e6
e6.next_node=e5
thisvalue=e1
while thisvalue:
    print(thisvalue.value)
    thisvalue=thisvalue.next_node
