## 입력
n, m = map(int, input().split()) # n = 나무수, m = 집으로 가져가려는 나무 길이
trees = list(map(int,input().split())) # 나무 높이가 저장된 리스트
# 탐색 대상: 절단할 높이
start, end = 1, sum(trees)

while start <= end:
    mid = (start + end) // 2 
    take = 0 #take의 위치가 관건 -> 가져갈 나무들의 합 언제 초기화?(탐색할 때마다 초기화)

    for tree in trees:
        # 나무 높이가 mid보다 크면
        if tree > mid:
            # 절단 가능
            take += tree - mid
    
    # 목표량을 달성하면 얘는 최대가 아님. 재탐색
    if take >= m:
        start = mid + 1
    # 목표량을 달성 못하면 좀 더 낮은 값들에서 재탐색
    else:
        end = mid - 1
        
print(end)
    