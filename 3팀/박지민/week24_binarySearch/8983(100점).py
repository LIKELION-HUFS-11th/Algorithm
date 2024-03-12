## 입력
m, n, l = tuple(map(int, input().split())) 
shoot_list = list(map(int, input().split())) # 총쏘는 위치
animal_list = [ tuple(map(int, input().split())) for _ in range(n)]

# 사대 위치 정렬
# [1,4,6,9]
# start, mid, end
shoot_list.sort() 

# 사대 위치에 대해 이진 탐색
# 그 동물에 대해서
# 그 동물이 잡히는 사대를 탐색함
cnt = 0
# (7,2)에 위치한 동물에 대해 그 동물이 잡히는 사대를 탐색함
for animal in animal_list:
    x, y = animal
    start, end = 0, m-1
    while start <= end:
        mid = (start + end) // 2
        dist = abs(shoot_list[mid] - x) + y
        if dist <= l:
            cnt += 1
            break #이래야 중복이 생기지 않음 (그 동물에 대해서는 동물이 잡히는 사대 탐색을 끝냄)
        elif shoot_list[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

print(cnt)