
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.front = self.rear = -1
        self.size = k #큐의 최대길이 저장

    def enQueue(self, value: int):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        
        self.queue[self.rear] = value
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            if self.front == self.size -1:
                self.queue[self.front] = None
                self.front = 0
            else:
                self.queue[self.front] = None
                self.front += 1

        return True   

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1
        
    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()