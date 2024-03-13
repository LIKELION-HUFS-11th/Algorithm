import sys
input = sys.stdin.readline

# #노드로 하면 중복? 이 애매하다.
# class Node:
#     def __init__(self):
#         self.

global cnt_points, result

def dfs(v, i, cnt): #현재 방문한 startpoint, 다음으론 몇번째 점을 방문해야하는지
    global cnt_points, result
    
    if cnt == cnt_points: #모든 점을 방문함
        return
    
    if i > len(blank[v][1]) - 1: #해당 점에서 갈수있는 모든 점을 감
        return #그냥 종료하면 되나..?

    if blank[v][0] == True: #이미 방문함 -> 다음점
        return dfs(next, i+1, cnt)
    
    blank[v][0] = True
    next = blank[v][1][0] #다음 방문할 점 (작은 점부터)
    return dfs(next, 0, cnt+1)


# 해결 X
def bfs(v, i, cnt): #v=세로이동, i=가로(?)이동
    global cnt_points, result

    if cnt == cnt_points:
        return
    
    if i > len(blank[v][1]) - 1: #모든 점 방문 -> 다음 깊이로
        next = blank[v][1][0]
        return bfs(next, 0, cnt)
    
    if blank[v][0] == True:
        return bfs(v, i+1, cnt)


    blank[v][0] = True
    next = blank[v][1][i+1]
    return bfs(v, i+1, cnt+1)



n, m, v = map(int, input().split())

blank = dict() #{ start: [visited, [end1, end2, ...]]}
for _ in range(m):
    x, y = map(int, input().split())

    if x in blank.keys():
        blank[x][1].append(y)
    else:
        blank[x] = [False, [y]]

    if y in blank.keys():
        blank[y][1].append(x)
    else:
        blank[y] = [False, [x]]

    

for elem in blank.keys():
    blank[elem][1].sort()

cnt_points = len(blank.keys())

result = []
dfs(v, 0, 1)
for elem in result:
    print(elem, end=" ")

result = []
bfs(v, 0, 1)
for elem in result:
    print(elem, end=" ")