n, k = map(int, input().split())
nList = []
for i in range(1, n+1):
    nList.append(i)
ans=[]

idx = k-1 #0부터 시작하는 인덱스이므로 1빼는것
count = 1


for _ in range(n-1):
  ans.append(nList.pop(idx)) #이동해서 빼기
  
  idx = idx+k-1 #다음 인덱스로 이동
  
  if idx>=len(nList): #배열의 끝에 왔을 때.
    idx = idx%len(nList)

#이하 출력
print("<", end='')
for elem in ans:
    print(elem, end=', ')
    
print(nList[0], ">", sep="")


# n, k = map(int, input().split())
# class CircleQueue:

#     rear = 0
#     front = 0
#     max_size = n+1
#     queue = list()
 
#     def __init__(self):
#         self.rear, self.front = 0, 0
#         self.queue = [0 for i in range(self.max_size)]
    
#     def is_empty(self):
#         if self.rear == self.front:
#             return True
#         return False
    
#     def is_full(self):
#         if (self.rear+1) %self.max_size == self.front:
#             return True
#         return False
    
#     def enqueue(self, x):
#         if self.is_full():
#             print('full')
#             return
#         self.rear = (self.rear+1) % (self.max_size)
#         self.queue[self.rear] = x
    
#     def dequeue(self):
#         if self.is_empty():
#             print('empty')
#         self.front = (self.front+1) % self.max_size
#         return self.queue[self.front]
    
#     def get_front_next(self):
#         return self.queue[self.front+1]
    
#     def queue_print(self):
#         i = self.front
#         if self.is_empty():
#             print("EMPTY QUEUE")
#             return
#         while True:
#             i = (i+1) % self.max_size
#             print(self.queue[i], ' ')
#             if i == self.rear:
#                 break



# C = CircleQueue()
# ans = []#정답 담을 리스트
# que  = []

# #0.원형큐에 담기
# for i in range(1, n+1):
#     C.enqueue(i)


# # fr = C.front
# # rr = C.rear


# while not C.is_empty():
#     temp = []
#     #1 목적지까지 deque
#     for i in range(k):
  
#         if i == k-1:
#             ans.append(C.dequeue())
#         else:
#             temp.append(C.dequeue())
    
#     for elem in temp:
#         C.enqueue(elem)  
#     # if x1:
#     #     C.enqueue(x1)
#     # if x2:
#     #     C.enqueue(x2)
    
#     #2 뒤에 지운 애들 중 필요한 애들 enque
#     # f_n = C.get_front_next()
#     # for i in range(f_n-3, f_n-1):
#     #     C.enqueue(i)
#     C.queue_print()
#     r = C.rear
    

# print(ans)



