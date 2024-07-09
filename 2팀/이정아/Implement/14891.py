import sys
input = sys.stdin.readline
from  collections import deque

'''
[구현]
1. 돌려야 하는 횟수 K가 100 이하로 작음 => 이중 for문 써도 되겠다
2. 회전시킬 톱니바퀴 번호에 따라 영향받는 순서가 고정됨 + 4가지밖에 없음
    ex. 1 => 1-2, 2-3, 3-4 // 2 => 2-1, 2-3, 3-4 // 3 => 3-4, 3-2, 2-1 // 4 => 4-3, 3-2, 2-1
3. 맞닿은 부분 idx가 톱니바퀴가 상대적으로 왼쪽에 위치했냐 오른쪽에 위치했냐에 따라 2, 6으로 고정
    & 왼쪽에 위치했는지 오른쪽에 위치했는지는 톱니바퀴 번호끼리 비교해 알 수 있음
'''

gears = [] # 톱니바퀴 초기 상태 ex. [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], ...]
# 회전시킬 때 popleft, appendleft를 사용하기 위해 deque로 처리
for _ in range(4):
    gears.append(deque([int(char) for char in input().rstrip()]))

rotations = [] # 톱니바퀴 회전시키는 방법 ex. [[3, -1], [1, 1]]
k = int(input().rstrip())
for _ in range(k):
    rotations.append(list(map(int, input().split())))

def clockwise(dq:deque): # 톱니바퀴 시계방향으로 회전시키기
    dq.appendleft(dq.pop())
    return dq

def c_clockwise(dq:deque): # 톱니바퀴 반시계방향으로 회전시키기
    dq.append(dq.popleft())
    return dq

# 회전시킬 톱니바퀴 번호에 따라 고정되는, 영향받는 톱니바퀴 순서. [영향주는 톱니바퀴, 영향받는 톱니바퀴]
orders = [[[0, 1], [1, 2], [2, 3]], [[1, 0], [1, 2], [2, 3]], [[2, 3], [2, 1], [1, 0]], [[3, 2], [2, 1], [1, 0]]]

# gear : 돌릴 톱니바퀴 번호, direction : 1이면 시계방향, -1이면 반시계방향
for gear, direction in rotations:
    dirs = [0] * 4 # 이번 회전에서 몇 번 톱니바퀴를 무슨 방향으로 돌릴 것인지. 0이면 안 돌리고 놔둠. 1이면 시계방향, -1이면 반시계방향
    dirs[gear-1] = direction # 돌릴 톱니바퀴 번호는 1부터 시작하므로 -1 빼주고 dirs 리스트에 방향 저장
    now_orders = orders[gear-1] # 돌릴 톱니바퀴 번호에 따라, orders로부터 톱니바퀴 영향 줄 순서 가져옴
    for now_order in now_orders:
        if gears[min(now_order)][2] != gears[max(now_order)][6]: # now_order는 길이 2짜리 리스트이므로 min, max 활용해 어느 톱니바퀴가 왼쪽이고 오른쪽인지 판단+비교
                dirs[now_order[1]] = dirs[now_order[0]] * -1 # now_order의 첫 번째 원소로 인해 두 번째 원소가 영향 받음
                                                             # => 서로 n, s극으로 다르면 두 번째 원소(영향받는 친구)를 첫 번째 톱니바퀴(영향주는 친구)를 돌려야 하는 방향의 반대방향으로 돌리겠다고 dirs에 저장
                                                             # => 서로 극이 같으면 영향받는 친구를 안 돌려도 됨 -> 그냥 0인 채로 dirs 그대로 두기
    for i in range(4): # dirs에 저장한 대로 돌려주기. 1이면 시계방향, -1이면 반시계방향, 0이면 놔두기
        if dirs[i] == 1:
            gears[i] = clockwise(gears[i])
        elif dirs[i] == -1:
            gears[i] = c_clockwise(gears[i])

ans = 0
for j in range(4):
    if gears[j][0] == 1:
        ans += 2**j
print(ans)