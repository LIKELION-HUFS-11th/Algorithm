import sys
input = sys.stdin.readline

c = int(input())  # 테스트케이스 개수

def lineup(num, sums):  # 배치할 선수 인덱스, 현재까지 배치된 선수들의 능력치 합
    global max_str
    if num == 11:
        max_str = max(max_str, sums)  # 최고값 갱신
        return
    
    for i in range(11):
        if member[i] or not info[num][i]:  # 이미 배정된 멤버이거나, 해당 포지션의 능력치가 0
            continue

        member[i] = 1  # 포지션에 배치
        lineup(num + 1, sums + info[num][i])  # 다음 선수 배치 시도
        member[i] = 0  # 원래 상태로 되돌리기

for _ in range(c):
    info = [list(map(int, input().split())) for _ in range(11)]
    max_str = 0  # 초기 최댓값
    member = [0] * 11  # 포지션 체크용

    lineup(0, 0)  # 0번 선수부터, 현재까지 능력치 합은 0
    print(max_str)

'''
[[100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 80, 70, 70, 60, 0, 0, 0, 0, 0, 0], 
 [0, 40, 90, 90, 40, 0, 0, 0, 0, 0, 0], 
 [0, 40, 85, 85, 33, 0, 0, 0, 0, 0, 0], 
 [0, 70, 60, 60, 85, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 95, 70, 60, 60, 0, 0], 
 [0, 45, 0, 0, 0, 80, 90, 50, 70, 0, 0], 
 [0, 0, 0, 0, 0, 40, 90, 90, 40, 70, 0], 
 [0, 0, 0, 0, 0, 0, 50, 70, 85, 50, 0], 
 [0, 0, 0, 0, 0, 0, 66, 60, 0, 80, 80], 
 [0, 0, 0, 0, 0, 0, 50, 50, 0, 90, 88]]
'''