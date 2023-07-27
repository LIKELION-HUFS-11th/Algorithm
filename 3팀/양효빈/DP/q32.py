# dp 문제
# 1. 최적 부분 구조: 큰 문제를 작은 문제로 나누고 작은 문제의 답을 모아 큰 문제 해결
# 2. 중복되는 부분 문제: 동일하게 반복되는 작은 문제로 해결해야 한다

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = []
tmp = arr[0][0]


def right(arr, a, b, tmp, result):
    if a >= n-1:
        result.append(tmp)
        return result
    else:
        tmp += arr[a][b]
        right(arr, a+1, b, tmp, result)
        left(arr, a+1, b+1, tmp, result)


def left(arr, a, b, tmp, result):
    if a >= n-1:
        result.append(tmp)
        return result
    else:
        tmp += arr[a][b]
        right(arr, a+1, b, tmp, result)
        left(arr, a+1, b+1, tmp, result)


def path(arr, tmp, result):
    i, j = 0, 0

    right(arr, i+1, j, tmp, result)
    left(arr, i+1, j+1, tmp, result)
    return result

result = max(result)

print(result)

