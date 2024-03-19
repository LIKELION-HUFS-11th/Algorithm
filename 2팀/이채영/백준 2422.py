import sys
input = sys.stdin.readline

from itertools import combinations #조합 - 중복 허용 x, 순서 고려 x (좋은 라이브러리..)

"""
sol1) 조건에 맞는 조합들만 뽑기

"""

n, m = map(int, input().split())

icecream = list(range(1, n+1))
avoid = {} # value = key아이스크림과 조합되면 >안되는< 아이스크림 리스트


for i in range(1, n+1):
    avoid[i] = [i] #자기자신과 조합되면 안되므로 기본적으로 자기자신 추가 (조합하면 안되는 아이스크림이 없는 것도 있을 수 있으므로 미리 설정해야함)


for _ in range(m): 
    a = list(map(int, input().split()))

    avoid[a[0]].append(a[1])
    avoid[a[1]].append(a[0]) #한쪽에만 저장 x 각각 저장해야 함


cnt = 0
for i in range(1, n): # i = 조합의 기준이 되는 아이스크림/ 마지막 맛은 볼 필요 없음
    not_avoid = list(set(icecream) - set(avoid[i])) #i 기준 조합이 가능한 아이스크림 리스트) 아이스크림 리스트 - 피해야하는 아이스크림 리스트

    not_avoid.sort()
    not_avoid = [elem for elem in not_avoid if elem >= i] #중복방지 -> 기준이 되는 아이스크림보다 큰 번호끼리만 조합할 것. (134/ 314가 있으면 314는 고려하지 않는다는 뜻)
    
    #리스트 안의 원소를 돌때는 가급적 리스트원소에 변동이 없어야 함
    # for elem in not_avoid:
    #     if elem >= i:
    #         index = not_avoid.index(elem)
    #         del not_avoid[:index] #중복방지

    #         break
    

    comb = list(combinations(not_avoid, 2)) #1개는 고정이므로 2개 조합


    if comb: #comb의 원소(2개)끼리도 조합 체크
        comb = [elem for elem in comb if elem[0] not in avoid[elem[1]]]


    cnt += len(comb)

print(cnt)




"""
sol2) 
3개로 조합의 개수가 정해져있으므로 sol1으로도 풀 수 있지만,
더 많은 경우를 생각해 >브루트포스(모든 조합을 생성한 후 조건에 맞지 않는 것 제외시키기)<로 풀기를 권장~.~

"""

n, m = map(int, input().split())
icecream = [[False for _ in range(n+1)] for _ in range(n+1)] #icecream[x][y] = x번과 y번 아이스크림이 어울리지 않는 조합인지 저장

for i in range(m):
    i1, i2 = map(int, input().split())

    #어울리지 않는 조합이면 True
    icecream[i1][i2] = True
    icecream[i2][i1] = True #마찬가지로 양쪽에 모두 저장해야함

result = 0
for a, b, c in combinations(range(1, n+1), 3): #1~n의 모든 조합 생성
    if icecream[a][b] or icecream[a][c] or icecream[b][c]: #마찬가지로 [b][a], [c][a], [c][b] 케이스는 확인하지 않음 (중복방지)
        continue #한 쌍이라도 어울리지 않는 조합이라면 탈락

    result += 1

print(result)