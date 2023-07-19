# n 입력
n = int(input())
# house_locations 입력
house_locations = list(map(int, input().split()))

# 설계
# house_locations 정렬
house_locations.sort()

# mid_idx
mid_idx = (n-1) // 2

# 출력
print(house_locations[mid_idx])