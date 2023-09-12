class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k

    def enQueue(self, value: int) -> bool:
        if isFull(self.q):
            return False
        else:
            i = 0
            while i < len(self.q):
                if self.q[i] == None:
                    self.q[i] == value
                    return true

    def deQueue(self) -> bool:
        if isEmpty(self.q) == False:
            i = 0
            while i < len(self.q):

    def Front(self) -> int:
        if ieEmpty(self.q) == True:
            return -1
        else:
            return self.q[0]

    def Rear(self) -> int:

    def isEmpty(self) -> bool:
        isempty = True
        for i in self.q:
            if i == None:
                isempty = True
            else:
                isempty = False
        return isempty

    def isFull(self) -> bool:
        isfull = True
        for i in self.q:
            if i == None:
                isfull = False
            else:
                isfull = True
        return isfull


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
