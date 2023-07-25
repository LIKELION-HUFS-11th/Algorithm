# 떡볶이 떡 만들기
# 1. 리스트에 가장 긴 떡 - 0 ~ 가장 긴 떡 길이 저장
# 2. 이진 탐색을 통해서 최대로 절단할 수 있는 길이 찾음
# 2-1. 중간값일 때, 남은 길이의 합이 m보다 작으면 왼쪽 탐색
# 2-2. 중간값일 때, 남은 길이의 합이 m보다 크면 오른쪽 탐색
# 2-3. 중간값일 때, 남은 길이의 합이 m과 같으면 return

def binary_search(start, end, target):
    result = 0
    if start >= end:
        return mid_num
    mid_num = (start + end) // 2
    for h in height:
        if h >= mid_num:
            result += (h-mid_num)
    if result > target:
        return binary_search(mid_num+1, end, target)
    elif result < target:
        return binary_search(start, mid_num-1, target)
    else:
        return mid_num


n, m = map(int, input().split())
height = list(map(int, input().split()))
print(binary_search(0, max(height), m))