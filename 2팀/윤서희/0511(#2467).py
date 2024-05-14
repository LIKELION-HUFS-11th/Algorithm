import sys
input = sys.stdin.readline

n = int(input())  # 용액의 수   
liq = list(map(int, input().split()))  # 용액의 특성값 (이미 오름차순)

# 투포인터를 위한 첫번째, 마지막 인덱스
start = 0   
end = n - 1  

# 두 용액 혼합값의 최솟값
min_num = abs(liq[start] + liq[end])

# 정답 용액
liq_1 = 0
liq_2 = n - 1

while start < end:
    sum = liq[start] + liq[end]

    # 두 용액 혼합값의 절대값이 최소라면 최솟값 및 인덱스 갱신
    if abs(sum) < min_num:
        min_num = abs(sum)
        liq_1 = start
        liq_2 = end

        # 두 용액 혼합값의 절대값이 0이라면 루프 종료
        if abs(sum) == 0:
            break
    
    # 두 용액 혼합값의 부호에 따라 인덱스 변경
    if sum < 0:
        start += 1
    if sum > 0:
        end -= 1


print(liq[liq_1], liq[liq_2])