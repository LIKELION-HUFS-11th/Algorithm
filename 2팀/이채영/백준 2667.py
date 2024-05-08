import sys
input = sys.stdin.readline

"""
백트래킹
"""
global n, cnt


def find_area(x, y):
    global n, cnt

    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return #범위 끝까지 도달하면 다시 돌아감
    
    #동서남북 체크
    
    if arr_2d[x][y] == 1:
        cnt += 1
        arr_2d[x][y] = 0
    
        find_area(x+1, y) #한칸아래
        find_area(x, y+1) #한칸오른쪽
        find_area(x, y-1) #한칸왼쪽
        find_area(x-1, y) #한칸위

n = int(input().strip())

arr_2d = []

for i in range(n):
    arr_2d.append(list(map(int, input().strip())))

houses = []
cnt = 0
for i in range(n):
    for j in range(n):
        if arr_2d[i][j] == 1:
            find_area(i, j) 
            houses.append(cnt)
            cnt = 0

houses.sort()

print(len(houses))
for elem in houses:
    print(elem)
