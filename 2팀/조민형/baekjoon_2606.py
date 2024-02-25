import sys

computer = int(sys.stdin.readline())
connect = int(sys.stdin.readline())

graph = [[]*computer for _ in range(computer+1)]

for _ in range(connect):
    connect_a, connect_b = map(int,sys.stdin.readline().split())
    graph[connect_a].append(connect_b)
    graph[connect_b].append(connect_a)

count = 0
visited =[0] * (computer+1)

def infected_search(computer=1):
    global count
    visited[computer] = 1
    for i in graph[computer]:
        if visited[i]==0:
            infected_search(i)
            count += 1

        
infected_search()
print(count)
    
