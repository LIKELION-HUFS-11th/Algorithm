import sys, math

case = int(sys.stdin.readline())
for i in range(case):
    choX, choY, choR, baekX, baekY, baekR = list(map(int,sys.stdin.readline().split()))
    # 두 터렛의 사이 거리 계산 -> 피타고라스 정리
    distance = math.sqrt((baekX-choX)**2 + (baekY-choY)**2)
    # 둘이 완전히 겹쳐서 위치가 무제한으로 나올때
    if distance == 0 and choR==baekR:
        print(-1)
    # 내접, 외접해서 한번만 겹칠 때
    elif abs(choR-baekR) == distance or choR+baekR==distance:
        print(1)
    # 두개의 점이 겹치는 경우
    elif abs(choR-baekR) < distance < choR + baekR:
        print(2)
    else:
        print(0)       
    