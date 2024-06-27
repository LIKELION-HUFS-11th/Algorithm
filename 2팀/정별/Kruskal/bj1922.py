#참고링크: https://seen-young.tistory.com/99
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
# nList = [list(map(int, input().split()))]
# print(nList)

parent = [i for i in range(n+1)] #각 정점 별 부모 저장. 처음에는 자기 자신이 부모임
edges = [] #간선 비용, 간선a, 간선b를 저장하여 오름차순으로 저장


def find_parent(x): #x노드의 루트노드 찾기.
    if parent[x] !=x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b): #두 집합 a, b 합치기
    a = find_parent(a)
    b = find_parent(b)
    if a<b: #두 노드를 비교해 작은 걸 부모로 설정. 인덱스가 자식, 값이 부모
        parent[b] = a
    else:
        parent[a] =b

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort() #가중치 기준 오름차순 정렬
ans =0
for c, a, b in edges:
    #두 정점 a와 b의 부모 다른지 확인
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans+=c

print(ans)


    
    