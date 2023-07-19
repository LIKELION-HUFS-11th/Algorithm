from collections import deque #collections 모듈에서 제공하는 deque 자료구조를 활용하겠다. 
                                #왜? 큐 구현하기 위해서

#큐 구현을 위해 deque 라이브러리 사용
queue = deque() #deque(덱)로 queue(큐)를 만들겠다

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.pop()
queue.append(1)
queue.append(4)
queue.pop()
print(queue)
queue.reverse() #역순으로 바꿔준 후에
print(queue) #다시 출력




