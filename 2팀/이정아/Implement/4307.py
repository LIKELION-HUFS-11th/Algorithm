import sys
input = sys.stdin.readline

'''
[구현]
1. 가장 빨리 다 떨어지는 시간 : 가장 중심점에 가까운 개미가 0, n 중 더 빨리 도달 가능한 지점에 도달하는 시간
2. 가장 늦게 다 떨어지는 시간 : 가장 0, n에 가까운 개미가 그 반대편에 도달하는 시간
* 개미가 만나서 방향이 바뀌는 것은 고려할 필요 없음! why) 어차피 만나서 방향 바뀌어봤자 개체만 바뀔 뿐 위치는 동일
ex. a, b 개미가 각각 4, 6에 존재
0초) a : 4, b : 6
1초) a : 5, b : 5
2초) a : 4, b : 6
만나도 방향이 바뀌지 않고 이를 무시한다면
0초) a : 4, b : 6
1초) a : 5, b : 5
2초) a : 6, b : 4
=> a, b의 전진 방향은 서로 다르지만 a, b가 아닌 둘 다 '개미'로만 본다면 결국 둘 다 6->4(왼쪽), 4->6(오른쪽)으로 동일하게 이동
'''

tc = int(input())
for _ in range(tc):
    l, n = map(int, input().split())
    ants = []
    fastest = 0
    slowest = 0
    
    for i in range(n):
        ant = int(input())
        ants.append(ant)
        fastest = max(fastest, min(abs(l-ant), ant))
        slowest = max(slowest, max(abs(l-ant), ant))
    
    print(fastest, slowest)