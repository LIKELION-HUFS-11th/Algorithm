## 입력
import sys
n = int(sys.stdin.readline()) #용액의 수
values = list(map(int,sys.stdin.readline().split())) #용액의 특성값이 저장된 리스트
values.sort() # 정렬

start, end = 0, n-1
min_sum = sys.maxsize

while start < end:
    take = values[start] + values[end]
    # 현재까지의 최소합보다 작으면
    if abs(take) < min_sum:
        # 갱신하고
        min_sum = abs(take)
        # 두 용액 저장
        result = [values[start], values[end]]
    # 합이 0보다 작으면 시작점 조정
    if take < 0:
        start += 1
    # 합이 0보다 크면 끝점 조정
    elif take > 0:
        end -= 1
    # 합=0이면 끝
    else:
        break

print(result[0],result[1])
    
    