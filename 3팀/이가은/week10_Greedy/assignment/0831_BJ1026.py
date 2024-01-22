'''
[보물]
https://www.acmicpc.net/problem/1026
'''
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)

result = 0
for i in range(n):
    result += A[i] * B[i]
    
print(result)
