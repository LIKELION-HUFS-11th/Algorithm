# 큐 (First In First Out)
    # 양쪽이 뚫려있고, 왼쪽으로 들어가면서 하나씩 밈

from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)    # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue)    # 나중에 들어온 원소부터 출력

'''
파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조 활용
* deque : 스택과 큐의 장점을 모두 채택한 것
    - 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적
    - queue 라이브러리를 이용하는 것보다 더 간단
    (대부분의 코테에서 collections 모듈과 같은 기본 라이브러리 사용 허용함)
'''