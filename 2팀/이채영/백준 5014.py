from collections import deque  
import sys  

"""  
f: 건물의 총 층 수  
s: 강호가 현재 있는 층 수  
g: 스타트링크의 층 수(타겟 층수)  
u: 위로 u층 만큼  
d: 아래로 d층 만큼  
"""  
f, s, g, u, d = map(int, sys.stdin.readline().split())  
check = [0 for _ in range(f + 1)]  # 층수별로 지금까지 방문한 층 개수 저장


def bfs():  
    queue = deque()  
    queue.append(s)  

    check[s] = 1  #시작점에서 시작했다고 1로 체크 (마지막 출력시 1을 빼야함)
                ## 예를 들어 입력이 10 10 1 0 1로 들어온 경우, 시작지점을 먼저 체크를 하지 않으면 10번 이동한 것으로 출력되지만 실제로는 9번만 이동합니다. 이 경우를 조심해야합니다.

    while queue:  
        y = queue.popleft()  

        if y == g:  ##현재층수 = 목표층수
            return check[y] - 1  
        else:  
            for x in (y + u, y - d):  # 위로 / 아래로 이동 각각 체크
                if (0 < x <= f) and check[x] == 0:  #방문한 적 없는 층이어야 함
                    check[x] = check[y] + 1  
                    queue.append(x)  
                    
    return "use the stairs"  #큐가 모두 종료될때까지 실행하면 use the stairs


print(bfs())





# global f, g, u, d, satisfied

# def up(arrive, cnt):
#     global f, g, u, d, satisfied
#     if arrive > f:
#         return -1
    
#     if arrive == g:
#         return cnt
    
#     elif arrive < g:
#         up(arrive+u, cnt+1)
    
#     else:
#         if satisfied: #한번 꺾지 않은 상태
#             satisfied = False
#             down(arrive-d, cnt+1)
#         else:
#             return -1


    
# def down(arrive, cnt):
#     global f, g, u, d, satisfied
#     if arrive < 1:
#         return -1
    
#     if arrive == g:
#         return cnt
    
#     elif arrive > g:
#         down(arrive-d, cnt+1)
    
#     else:
#         if satisfied:
#             satisfied = False
#             up(arrive+u, cnt+1)
#         else:
#             return -1


# f, s, g, u, d = tuple(map(int, input().split()))

# satisfied = True
# result = 0

# if g > s:
#     result = up(s+u, 1)
# elif g < s:
#     result = down(s-d, 1)

# else:
#     if u * d == 0:
#         if u == 0:
#             result += 1
#         if d == 0:
#             result += 1
#     else:
#         result = "use the stairs"

# if result == -1:
#     result = "use the stairs"

# print(result)
    