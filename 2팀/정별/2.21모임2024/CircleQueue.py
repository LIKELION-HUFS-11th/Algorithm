n, k = map(int, input().split())

class CircleQueue:

    rear = 0
    front = 0
    max_size = n + 1
    queue = list()
 
    def __init__(self):
        self.rear, self.front = 0, 0
        self.queue = [0 for i in range(self.max_size)]
    
    def is_empty(self):
        return self.rear == self.front
    
    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front
    
    def enqueue(self, x):
        if self.is_full():
            print('full')
            return
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = x
    
    def dequeue(self):
        if self.is_empty():
            print('empty')
            return None
        self.front = (self.front + 1) % self.max_size
        return self.queue[self.front]
    
    def get_front_index(self):  # front 메서드 이름 변경
        return self.front
    
    def queue_print(self):
        i = self.front
        if self.is_empty():
            print("EMPTY QUEUE")
            return
        while True:
            i = (i + 1) % self.max_size
            print(self.queue[i], end=' ')
            if i == self.rear:
                break
        print()

C = CircleQueue()
ans = []

for i in range(1, n+1):
    C.enqueue(i)
C.queue_print()

while not C.is_empty():  # is_empty 메서드 호출 수정

    for i in range(k):
        if i == k - 1:
            ans.append(C.dequeue())
        else:
            C.dequeue()
    
    front_index = C.get_front_index()  # front 변수 이름 변경
    for i in range(front_index, front_index + 2):  # enqueue 범위 수정
        C.enqueue(i)

print(ans)
