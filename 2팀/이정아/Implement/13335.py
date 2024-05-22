from collections import deque

n, max_length, max_weight = map(int, input().split())
trucks = deque(list(map(int, input().split()))) # 트럭 대기열

now_length, now_weight, time = 0, 0, 0 # 다리 위에 올라간 트럭 수, 다리 위에 올라간 트럭 총 무게, 소요시간(답)
q = deque([]) # 다리 위를 지나는 트럭들

# 대기열의 트럭이 다 지나갈 때까지. while문 한 번 도는 것 == 한 단위시간
while trucks:
    # 다리 위에 지나가는 중인 트럭이 있으면
    if q:
        for i in range(len(q)):
            q[i][1] -= 1 # 다리 위 트럭들의 다리 지나는 데에 걸리는 시간 -1
        if q[0][1] == 0: # 다리 다 지나갔으면
            truck = q.popleft() # 다리 위를 지나는 트럭에서 제외
            now_length -= 1 # 다리 위에 올라간 트럭 수 -1
            now_weight -= truck[0] # 다리 위에 올라간 트럭 총 무게 -다리 다 지나간 트럭 무게
    if now_length < max_length and now_weight+trucks[0] <= max_weight: # 새로운 트럭이 다리에 올라갈 수 있으면
        truck = trucks.popleft() # 트럭 대기열에서 새로운 트럭 빼서 다리 위에 올리기
        now_length += 1 # 다리 위에 올라간 트럭 수 +1
        now_weight += truck # 다리 위에 올라간 트럭 총 무게 +새로운 트럭 무게
        q.append([truck, max_length]) # [트럭 무게, 다리 지나는 데에 걸리는 시간]
    time += 1
    
print(time+max_length) # 마지막 트럭이 다리에 올라간 시점 + 다리 다 지나는 데에 걸리는 시간(max_length)
    