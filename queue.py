class Queue:
    def __init__(self):
        self.queue=list()
    def add(self,dataval):
        if dataval is not self.queue:
            self.queue.insert(0,dataval)
            return True
        else:
            return False
    def size(self):
        return self.queue
    def sizee(self):
        return len(self.queue)
thequeue=Queue()
thequeue.add('mon')
thequeue.add('tue')
thequeue.add('wed')
thequeue.add('wed')
thequeue.add('thur')
thequeue.add('fri')
thequeue.add('sat')
thequeue.add('sun')
print(thequeue.size())
print(thequeue.sizee())