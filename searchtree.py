class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.leftval=None
        self.rightval=None
    def insert(self,dataval):
        if self.dataval:
            if dataval < self.dataval:
                if self.leftval is None:
                    self.leftval=Node(dataval)
                else:
                    self.leftval.insert(dataval)
            else dataval > self.dataval:
                if self.rightval is None:
                    self.rightval=Node(dataval)
                else:
                    self.rightval.insert(dataval)
        else:
            self.dataval=dataval
    def findval(self,ikpval):
        if ikpval < self.dataval:
            if self.leftval is None:
                return str(ikpval)+'Not found'
            return self.leftval.findval(ikpval)
        else if ikpval > self.dataval:
            if self.rightval is None:
                return str(ikpval)+'not found'
            return self.rightval.findval(ikpval)
        else:
            print(str(self.dataval) + 'is found')
    def printress(self):
        if self.leftval:
            self.leftval.printree()
            print(self.dataval)
        if self.rightval:
            self.rightval.printree()
            print(self.rightval)
root =Node()
root.insert(00)
root.insert(90)
root.insert(29)
root.insert(34)
print(root.findval(7))
print(root.findval(00))
