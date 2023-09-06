import sys
## 입력
n = int(sys.stdin.readline()) # 지방의 수 n
requests = list(map(int,sys.stdin.readline().split())) # 각 지방의 예산요청 리스트
limit = int(sys.stdin.readline())

# 탐색 대상 : 상한액 -> 
start, end = 1, sum(requests)

# 모든 요청대로 예산 배정이 가능하다면
if end <= limit:
    # 요청 중 최대의 값을 배정
    print(max(requests))

else:
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for request in requests:
            # 상한액보다 높다면
            if request > mid:
                # 상한액을 배정
                total += mid
            else:
                total += request
        # total이 총예산보다 작다면 시작점 조정해서 재탐색
        if total < limit:
            start = mid + 1
        # total이 총예산을 넘어선다면, 끝점 조정해서 재탐색
        else:
            end = mid - 1

    print(end)



