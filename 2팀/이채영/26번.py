class MyCircularDeque:
    def __init__(self, k):
        self.size = k
        self.front = 0 #제일 앞자리보다 한자리 앞
        self.rear = 0
        self.items = [None] * k
    
    #[fr, _, _, _, _, _]    
    def insertFront(self, item): #front에 삽입 - 하나 앞으로 front 수정
        if not self.isFull(): 
            self.items[self.front] = item
            self.front = (self.front - 1 + self.size) % self.size 

    def insertLast(self, item): #rear에 삽입 - 하나 뒤로 rear 수정 후 삽입
        if not self.isFull(): 
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = item

    def deleteFront(self): #front 삭제 - 하나 뒤로 front 수정하여 front
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
            self.items.pop(self.front)
            return self.items[self.front]
    
    def deleteLast(self): #rear 삭제 - 
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = (self.rear - 1 + self.size) % self.size
            return item
        
    def getFront(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % self.size]
    
    def getRear(self):
        return self.items[self.rear]
    
    def isEmpty(self): #공백 : front = rear
        return self.front == self.rear 

    def isFull(self): #포화 : front가 rear보다 하나 앞
        return self.front == (self.rear + 1) % self.size
    


###DriverCode
dq = MyCircularDeque(10)
for i in range(9): #포화상태를 생각하면 MAXQSIZE가 10일때 이게 최대
    if i in range(9):
        if i % 2 == 0:
            dq.insertLast(i)
        else:
            dq.insertFront(i)
# dq.display()

for _ in range(2):
    dq.deleteFront()
for _ in range(3):
    dq.deleteLast()
# dq.display() #여기 값이 자꾸 [1, 0, 2, 4]로 되는데 왜이러냐

for i in range(9,14):
    dq.insertFront(i)
# dq.display()
