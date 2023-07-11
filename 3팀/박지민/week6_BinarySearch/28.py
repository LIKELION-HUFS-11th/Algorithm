def fixed_point(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 고정점을 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid] > mid:
        return fixed_point(array, start, mid-1)
    # 중간점이 가리키는 위치의 값보다 중간점이 큰 경우 오른쪽 확인
    else:
        return fixed_point(array, mid+1, end)

n = int(input())
array = list(map(int, input().split()))

point = fixed_point(array, 0, n-1)
if point == None:
    print(-1)
else:
    print(point)