### 이진탐색
# 리스트 내에서 데이터를 빠르게 탐색하는 알고리즘
# 순차탐색: 앞에서부터 차례대로

## 이진탐색: 반으로 쪼개면서 탐색하기
# 배열 내부 데이터가 정렬되어 있어야 함
# 절반 쪼갤 때 소수점 버림
# 이진탐색 알고리즘은 꼭꼭 외우기!!

# 재귀함수로 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1) # 몇 번째에 있는지 반환(1부터)


# 반복문으로 구현한 이진 탐색 소스코드
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)