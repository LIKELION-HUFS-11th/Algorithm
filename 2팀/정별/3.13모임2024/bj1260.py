import sys
n, m, v = map(int, sys.stdin.readline().split())

hitmap = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())

    hitmap[x][y]=1
    hitmap[y][x]=1

# print(hitmap)

nList = [0]*(n+1) #방문여부
#dfs 출력
def dfs(v):
    nList[v]=1
    print(v, end=' ')
    for i in range(1, n+1):
        if(nList[i]== 0 and hitmap[v][i]==1):
            dfs(i)

#bfs 출력

def bfs(v): #큐로 진행
    queue=[v] #들려야 할 정점 저장
    nList[v]=0 #방문한 지점 0으로 표시
    while queue:
        v=queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            
            if(nList[i]==1 and hitmap[v][i]==1):
                queue.append(i)
        
                nList[i]=0
dfs(v)
print()
bfs(v)