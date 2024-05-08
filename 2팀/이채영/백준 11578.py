"""
그리디 -> 반드시 정답이진 않음

1. 그냥 모든 문제를 다 풀 수 있는 조합 구하기 : combinations
2. 최소 조합 찾기

문제, 팀원수가 10, 시간제한 2초로 최악의 경우에도 시간초과 우려 덜함

"""

import sys
input = sys.stdin.readline

from itertools import combinations

# 모든 문제를 풂 + 팀원의 수 최소화 

n, m = tuple(map(int, input().split()))

candidate = {}
for i in range(m):
    able = list(map(int, input().split()))
    num = able.pop(0) #문제 개수

    candidate[i] = able


total_satisfied = False
for i in range(1, m+1):
    combi = list(combinations(range(m), i)) #가능한 i개 선택 조합

    
    for stu in combi: #ex. (0, 1, 3번 학생) 하나의 조합 탐색
        solved = [0 for _ in range(n)]
        for s in stu: #1번학생 
            for q in candidate[s]: #1번학생 -> 1,3,4 문제
                solved[q-1] = 1 #문제번호가 1번부터임
        
        satisfied = True
        for elem in solved:
            if elem == 0:
                satisfied = False
                break

        if satisfied: #모든 문제를 푸는 조합 찾음
            total_satisfied = True
            result = i
            break
        else:
            continue #다른 조합으로 계속 탐색

    if total_satisfied:
        break
    else:
        continue


if total_satisfied:
    print(result)
else:
    print(-1)
    
