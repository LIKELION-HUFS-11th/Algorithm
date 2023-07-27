import collections  # defaultdict를 쓰기위래

nums = [-1, 0, 1, 2, -1, -4]

nums.sort()
# nums = [-4,-1,-1,0,1,2]
lists = collections.defaultdict(list)
# key error 없이 바로 아이템을 생성시켜주기 위해서, 그 아이템은 리스트형

for i in range(len(nums)-2):
    # 브루트 포스 방식 사용, 배열을 여러번 반복하여 모든 조합을 무차별적으로 확인하는 대입방식
    # 이 경우에서는 가능한 num[i],num[k],num[j]의 조합을 모두 확인하기 위해 배열 3번 반복
    for k in range(i+1, len(nums)-1):
        for j in range(k+1, len(nums)):
            if nums[j] + nums[i] + nums[k] == 0:  # 조합의 합이 0이면
                lists[i].append(nums[i])
                # defaultdict의 i번째 인덱스에 해당하는 리스트에 세 조합 추가
                lists[i].append(nums[k])
                lists[i].append(nums[j])
        if nums[j] + nums[i] + nums[k] == 0:
            break  # 새로운 조합은 defaultdict의 다른 인덱스에 넣어야하기 때문


print(list(lists.values()))
