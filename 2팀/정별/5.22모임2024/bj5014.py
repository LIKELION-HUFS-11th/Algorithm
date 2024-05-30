import sys

from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())

#f 총 건물 층수
#s 현재 강호 위치
#g 스타트링크 위치

#u 위로 u층 이동
#d 아래로 d층 이동
    #만약 이동 할 장소 끝이면 안 움직임
    
#G층 못간다면 출력

#+u -d를 계속 반복하면서 g층으로 이동

visited = [0] * (f+1)
queue = deque([(s, 0)])
flag = False

# print(queue.popleft())
while queue:
    cur_floor, cnt= queue.popleft()
    # print(cur_floor, cnt)
    
    if cur_floor == g:
        print(cnt)
        flag = True
        exit()
    
    if visited[cur_floor]:
        continue
    
    visited[cur_floor] = True
    nUp = cur_floor + u
    nDown = cur_floor - d

    if nUp <= f:
        queue.append((nUp, cnt + 1))
    if nDown > 0:
        queue.append((nDown, cnt+1))

if not flag:
    print("use the stairs")


#재귀 방법. 런타임에러 걸림
# visited = [0] * (f+1)

# pointer = s #이동 포인터
# cnt = 0#버튼 수 최솟값
# flag = False #찾았는지 여부 확인

# def bfs(i,cnt):
#     global flag, visited
    
#     if i<=0 or f<i: #범위 벗어나는것 미리 커트
#         return
    
#     if i == g:
#         flag = True
#         print(cnt)
#         exit()
    
#     if visited[i]:
#         return
#     visited[i] = True
    
#     #올라가는 경우 내려가는 경우 다르게 처리
#     nUp = i+u
#     nDown = i-d
    
#     if i<=f:
#         bfs(nUp, cnt+1)
    
#     if 0<i :
#         bfs(nDown, cnt+1)
    
# bfs(pointer, 0)

# if not flag: #못찾았다면
#     print("use the stairs")



