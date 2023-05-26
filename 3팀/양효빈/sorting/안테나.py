# 입력
n = int(input())
arr = list(map(int, input().split()))

# 계수정렬
house = [0] * (max(arr)+1)

for h in arr:
    house[h] += 1


min_dis = float('inf')
antenna = 0
for i in range(len(house)):
    distance = 0
    if house[i]:
        for j in range(len(house)):
            if house[j]:
                distance += ( abs(i-j) * house[j] )
    
        if distance < min_dis:
            min_dis = distance
            antenna = i

print(antenna)