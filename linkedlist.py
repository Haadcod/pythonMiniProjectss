class Daynames:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.next_node=None
e1=Daynames('mon')
e2=Daynames('wed')
e3=Daynames('tue')
e4=Daynames('fri')
e5=Daynames('sun')
e6=Daynames('sat')
e7=Daynames('thu')
e1.next_node=e3
e3.next_node=e2
e2.next_node=e7
e7.next_node=e4
e4.next_node=e6
e6.next_node=e5
thisvalue = e1
while thisvalue:
    print(thisvalue.dataval)
    thisvalue=thisvalue.next_node