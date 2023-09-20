MAX_QSIZE = 10

class MyCircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self): #공백 상태도 추가..
        return self.front == self.rear 
    
    def isFull(self): #포화 : front가 rear보다 하나 앞
        return self.front == (self.rear + 1) % MAX_QSIZE
    
    def enQueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE #현재기준 rear 뒤에 삽입
            self.items[self.rear] = item
            return True

    def deQueue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QSIZE
            self.items.pop(self.front)
            return True

    def Front(self):
        if not self.isEmpty():
            return self.items[self.front]


    def Rear(self):
        if not self.isEmpty():
            return self.items[self.rear]
        
circularqueue = MyCircularQueue()

circularqueue.enQueue(10)
circularqueue.enQueue(20)
circularqueue.enQueue(30)
circularqueue.enQueue(40)
print(circularqueue.items)
circularqueue.Rear()
circularqueue.isFull()
circularqueue.deQueue()
circularqueue.deQueue()
print(circularqueue.items)
circularqueue.enQueue(50)
circularqueue.enQueue(60)
print(circularqueue.items)
r3 = circularqueue.Rear()
r4 = circularqueue.Front()