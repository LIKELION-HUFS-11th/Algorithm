### 예산 배정

# 모든 요청이 배정가능한 경우 요청 금액 그대로 배정
# 아닌 경우 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는
# 모두 상한액 배정, 상한액 이하일 경우에는 요청한 금액 그대로 배정

# 가능한 최대의 총 예산 배정
# 출력: 배정된 예산들 중 최댓값인 정수


# 지방의 수
n = int(input())
# 예산 리스트 + 오름차순 정렬
budget_list = list(map(int, input().split()))
budget_list.sort()
# 총 예산
total_budget = int(input())


def allocation(arr, budget):
    # 최소한 1의 예산은 각 지방에 분배되어야 하므로 left는 1로 설정
    left, right = 1, max(arr)
    
    while left <= right:
        mid = (left + right) // 2
        # 총예산을 넘지 않기 위해 min값 선택하여 sum
        total = sum(min(mid, x) for x in arr)
        
        # 상한값 올리기
        if total <= budget:
            left = mid + 1
        # 상한값 내리기
        else:
            right = mid - 1
    
    # left와 right 교차 시 값 반환
    return right

answer = allocation(budget_list, total_budget)
print(answer)


