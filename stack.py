class Stack:
    def __init__(self):
        self.stack=[]
    def add(self,dataval):
        if dataval is not self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    def peek(self):
        return self.stack[-1]
Astack=Stack()
Astack.add('monr')
Astack.add('tue')
Astack.peek()
print(Astack.peek())
Astack.add('wed')
Astack.add('thur')
Astack.add('fri')
Astack.add('sat')
Astack.add('sun')
print(Astack.peek())