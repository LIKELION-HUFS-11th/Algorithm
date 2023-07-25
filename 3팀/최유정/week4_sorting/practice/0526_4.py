# 두 배열의 원소 교체

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] > B[i]:
        break
    else:
        A[i], B[i] = B[i], A[i]

print(sum(A))