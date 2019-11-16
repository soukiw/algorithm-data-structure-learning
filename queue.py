# coding: utf-8
# Your code here!

#ring buffer
class Queue:

    def __init__(self,size=10):
        self.entries = [None for _ in range(size)]
        self.size = size
        self.front = self.rear = 0
        
    def next(self,n):
        return (n+1)%self.size
        
    def enqueue(self,n):
        if self.front == self.next(self.rear):
            print("queue is full")
            return False
            
        self.entries[self.rear]=n
        self.rear=self.next(self.rear)
        
    def dequeue(self):
        if self.front == self.rear:
            print("queue is enmpty")
            return False
            
        n = self.entries[self.front]
        self.front = self.next(self.front)
        return n
        
        
q=Queue(4)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.dequeue()
