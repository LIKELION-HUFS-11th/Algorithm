# 367p
# 모범답안 참고함
# O(logN)으로 설계해야 한다는 것이 핵심

def binary_count(array, target):

    n = len(array)

    left = binary_left(array, target, 0, n-1)
    if left == None:
        return 0

    right = binary_right(array, target, 0, n-1)

    return right - left + 1


def binary_left(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    
    if (mid == 0 or array[mid-1] < target) and array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_left(array, target, mid+1, end)
    else:
        return binary_left(array, target, start, mid-1)



def binary_right(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2

    if (mid == n-1 or target < array[mid+1]) and array[mid] == target:
        return mid
    elif array[mid] <= target:
        return binary_right(array, target, mid+1, end)
    else:
        return binary_right(array, target, start, mid-1)

n, target = map(int, input().split())
array = list(map(int, input().split()))

count = binary_count(array, target)

if count == None:
    print(-1)
else:
    print(count)