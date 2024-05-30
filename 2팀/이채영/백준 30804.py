import sys
input = sys.stdin.readline

global n

# 과일을 최소한으로 빼면서 두 종류 이하로 남도록 함 
# 슬라이딩 윈도우?

def sliding_window(a, b, cnt):
    global n
    if a > n - 2 or a < 0 or b < 1 or b > n-1:
        return
    if a > b+1:
        return
    
    left = set(tanghuru[a:b+1])

    if len(left) <= 2:
        nums.append(cnt)
        return
        #return cnt 하면 함수 종료가 안됨
    
    sliding_window(a+1, b, cnt+1)
    sliding_window(a, b-1, cnt+1)



n = int(input().strip())
tanghuru = list(map(int, input().split()))

nums = []

sliding_window(0, n-1, 0)

if nums:
    min_fruit = min(nums)
else:
    min_fruit = 0

print(n - min_fruit)



# for elem in list(map(int, input().split())):
#     deque.append(elem)

# for a in range(0, n-1):
#     for b in range(n, -1, -1):
   

# for문보다는 재귀가 나아보임
