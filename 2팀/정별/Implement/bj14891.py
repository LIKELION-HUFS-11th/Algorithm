import sys
from collections import deque
#deque의 rotate = -1이면 반시계 방향, 1이면 시계 방향 움직임

gears = {} #dict 형태로 key를 1~4번 톱니바퀴, 값을 n s 입력값들
for i in range(1, 5):
    # gears[i] = deque(list(map(int, sys.stdin.readline().reaplace("\n", ""))))
    #개행문자 제거
    gears[i] =deque(list(map(int, list(sys.stdin.readline().replace("\n", "")))))
n= int(input())

#가장 오른쪽인지 확인
def check_right(start, dir):
    #start 자리에 1~4번 들어갈 것임. 어떤 톱니바퀴를 점검하고 있는지
    #dir은 시계/반시계 방향 
    
    #더이상 조사 안되니 리턴
    if start > 4 or gears[start-1][2] == gears[start][6]:
        return
    #그외의 일반적인 경우, 오른쪽 확인
    if gears[start-1][2] != gears[start][6]:#n s로 서로 다르면
        check_right(start+1, -dir) #음수 붙임으로써 반대 회전
            #오른쪽 재귀로 끝까지 다 체크
        #그러고나서 회전
        gears[start].rotate(dir)

def check_left(start, dir):
    if start < 1 or gears[start][2] == gears[start+1][6]:
        return
    
    #위에 으론쪽 체크와 동일한 논리
    if gears[start+1][6] != gears[start][2]:
        check_left(start - 1, -dir)
        gears[start].rotate(dir)

for _ in range(n): #이제 돌린다
    num, dir = map(int, sys.stdin.readline().split())

    #오른쪽 왼쪽 회전 가능한지 둘다 확인하고 회전 시킴
    check_right(num+1, -dir) 
    check_left(num-1, -dir)
    
    #check 함수들에서 본인 회전하는 코드 마지막에 있음.
        #그래서 매개변수를 num+-1로 해두고, 본인은
        #현재 위치에서 돌리는 것임
    gears[num].rotate(dir)

res=0
for i in range(4):
    res += (2**i) * gears[i+1][0]
print(res)

