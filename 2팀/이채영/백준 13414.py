# 규칙 1, 2 : 중복될 경우 중복시점 기준 맨뒤로 보낸다.
import sys
input = sys.stdin.readline

k, l = map(int, input().split())


"""
Sol1. 선형탐색 - 시간초과
"""
## 리스트에 대한 in, remove 연산 : O(n) 
## 모든 요소를 순회하며 탐색하기 때문

register = []

for i in range(l):
    snum = input().strip()

    if snum in register:
        register.remove(snum)

    register.append(snum) #등록순서 맨뒤에 추가

for i in range(k):
    if i > len(register) - 1:
        break
    print(register[i])


"""
sol2. 힙소트 - 틀림..
"""



"""
sol3) 통과
"""
## 딕셔너리에 대한 in, del 연산 : O(1)
## 딕셔너리는 해시 테이블로 구현되어 있어 특정 키의 탐색을 상수시간에 할 수 있음!
    
s = dict()

for i in range(l):
    student = input().strip()
    if student in s.keys():
        del s[student]
        s[student] = 1

    if student not in s.keys():
        s[student] = 1

s = list(s.keys())

for i in range(k):
    try:
        print(s[i])
    except:
        pass