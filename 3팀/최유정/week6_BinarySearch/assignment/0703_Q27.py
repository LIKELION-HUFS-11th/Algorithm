# 정렬된 배열에서 특정 수의 개수 구하기
# 특정 수 시작하는 인덱스 + 끝나는 인덱스 찾기
# mid, mid+1이 각각 x-1, x인지 확인

n, x = map(int, input().split())
n_list = list(map(int, input().split()))

def binary_search_start(start, end, target):
    if start > end:
        return -1
    mid = (start + end) // 2
    if n_list[mid] == target:
        if n_list[mid-1] != target or mid == 0:
            return mid
        else:
            return binary_search_start(start, mid-1, target)
    elif n_list[mid] > target:
        return binary_search_start(start, mid-1, target)
    else:
        return binary_search_start(mid+1, end, target)

def binary_search_end(start, end, target):
    if start > end:
        return -1
    mid = (start + end) // 2
    if n_list[mid] == target:
        if n_list[mid+1] != target or mid == n-1:
            return mid
        else:
            return binary_search_end(mid+1, end, target)
    elif n_list[mid] > target:
        return binary_search_end(start, mid-1, target)
    else:
        return binary_search_end(mid+1, end, target)


start = binary_search_start(0, n-1, x)
if start == -1:
    print(-1)
else:
    print(binary_search_end(0, n-1, x) - start + 1)