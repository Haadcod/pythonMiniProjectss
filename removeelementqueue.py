class Queue:
    def __init__(self):
        self.queue=list()
    def add(self,dataval):
        if dataval is not self.queue:
            self.queue.insert(0,dataval)
            return True
        else:
            return False
    def removeof(self):
        if len(self.queue)>0:
            return self.queue.pop()
        else:
            return ('no element in the queue')
thequeue=Queue()
thequeue.add('mon')
thequeue.add('tue')
thequeue.add('wed')
thequeue.add('wed')
thequeue.add('thur')
thequeue.add('fri')
thequeue.add('sat')
thequeue.add('sun')
print(thequeue.removeof())
print(thequeue.removeof())
print(thequeue.removeof())
print(thequeue.removeof())