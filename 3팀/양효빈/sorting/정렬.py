### 1. 선택정렬
# 가장 작은 데이터와 맨 앞 데이터 바꾸기
# 다른 정렬 방법들에 비해 느린 편

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i] # 스와프

print(arr)



### 2. 삽입정렬
# 선택정렬에 비해 더 효율적, 데이터 정렬되어있을 때 더 효율적

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:
            break

print(arr)


### 3. 퀵 정렬
# 가장 많이 사용되는 알고리즘, 가장 빠름, O(NlogN)
# 이미 정렬되어 있을 때 가장 느리게 동작, O(N**2)
# pivot 사용

# 방법 1
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[pivot] = arr[pivot], arr[left]
    
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

quick_sort(arr, 0, len(arr)-1)
print(arr)


# 방법 2
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
    if len(arr) <= 1: return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))



### 계수 정렬
# 최솟값과 최댓값의 차이가 1,000,000을 넘지 않을 때 매우 효과적
# 모든 범위를 담을 수 이쓴 크기의 리스트를 선언해야 하므로
# 각 인덱스의 해당 값의 개수 저장 -> 출력
# 조건만 충족한다면 기수정렬과 더불어 가장 빠른 정렬 방법

arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(arr) + 1)

for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')


### 파이썬 내장 함수
# arr = sorted(arr)
# arr.sort()



















