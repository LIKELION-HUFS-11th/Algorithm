import sys
input = sys.stdin.readline

global DP

def len_triangle(n):
    global DP

    l = len(DP) - 1

    if n <= l:
        return DP[n]
    
    for i in range(l+1, n+1): #DP 계속 채우기
        DP.append(DP[i-1] + DP[i-5])

    return DP[n]



T = int(input().strip())

DP = [0, 1, 1, 1, 2, 2, 3] #N <= 100밖에 안되니까 애초에 100으로 만들어놔도 될듯

result = []
for _ in range(T):
    n = int(input().strip())

    length = len_triangle(n)
    result.append(length)

for elem in result:
    print(elem)