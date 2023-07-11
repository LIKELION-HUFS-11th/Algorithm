n = int(input())
array = list(map(int, input().split()))

def binary_search(array, start, end):
    if start >= end:
        return None
    
    if start == array[start]:
        return start
    elif end == array[end]:
        return end

    mid = (start+end) // 2

    if mid == array[mid]:
        return mid
    
    if binary_search(array, start, mid-1) != None:
        return binary_search(array, start, mid-1)
    elif binary_search(array, mid+1, end) != None:
        return binary_search(array, start, mid-1)


result = binary_search(array, 0, n-1)
if result == None:
    print(-1)
else:
    print(result)