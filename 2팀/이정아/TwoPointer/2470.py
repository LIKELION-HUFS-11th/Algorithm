n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

'''
[투포인터], [이진탐색] 중 투포인터
1. 왼쪽, 오른쪽에 각각 포인터 설정해두고
2. 해당 포인터의 값들을 더한 값의 절대값과, 이미 갖고 있는 합 최솟값 비교
3. 포인터 값들 더한 값의 절대값이 더 작으면 정답을 그 둘로 갱신
4. 포인터 값들 더한 값이 음수이면 0이 되기 위해 양수를 더 더해야 하므로 왼쪽 포인터를 오른쪽으로 옮김
5. 포인터 값들 더한 값이 양수이면 0이 되기 위해 음수를 더 더해야 하므로 오른쪽 포인터를 왼쪽으로 옮김
'''

answer = [liquids[0], liquids[-1]] # 정답 리스트 초기화
min = abs(liquids[0] + liquids[-1]) # 합 최솟값 초기화
left, right = 0, n-1 # 포인터 초기화

while left < right:
    l, r = liquids[left], liquids[right]
    total = l+r

    if abs(total) < min: # 3
        min = abs(total) # 3
        answer = [l, r] # 3
        if min == 0: # 포인터 값들 더한 값이 0이면 더 이상 찾아볼 필요 없이 바로 리턴
            break
    if total < 0: # 4
        left += 1
    else:
        right -= 1 # 5

print(*answer)

