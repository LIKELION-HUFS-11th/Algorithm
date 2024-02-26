import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))

max_time = sum(lectures)
longest = max(lectures)

def binary_search(max_time, target):
    global longest
    left, right = 0, max_time
    while left < right:
        mid = (left+right) // 2
        if mid < longest:
            left = mid + 1
            continue
        cnt = 0
        temp = 0
        for lecture in lectures:
            if temp+lecture > mid:
                cnt += 1
                temp = 0
            temp += lecture
        if cnt >= target:
            left = mid + 1
        else:
            right = mid
    return right
            
print(binary_search(max_time, m))