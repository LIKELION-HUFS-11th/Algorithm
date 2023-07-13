# 무지의 먹방 라이브

import heapq

# 팀원 풀이
def solution1(food_times, k):
    food_list = []
    food_cnt = len(food_times)

    for i in range(food_cnt):
        food_list.append([food_times[i], i+1])
    food_list.sort()

    cycle = 0
    for i, food in enumerate(food_list):
        check = food[0] - cycle
        if check:
            cnt = check * food_cnt
            if cnt <= k:
                k -= cnt
                cycle = food[0]
            else:
                k %= food_cnt
                new_food = food_list[i:]
                new_food.sort(key=lambda x:x[1])
                return new_food[k][1]
        food_cnt -= 1
    return -1

# 힙구조 이용
def solution2(food_times, k):
    answer = -1
    h = []
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i + 1))

    food_num = len(food_times)  # 남은 음식 개수
    previous = 0  # 이전에 제거한 음식의 food_time

    while h:
        # 먹는데 걸리는 시간: (남은 양) * (남은 음식 개수)
        t = (h[0][0] - previous) * food_num
        # 시간이 남을 경우 현재 음식 빼기
        if k >= t:
            k -= t
            previous, _ = heapq.heappop(h)
            food_num -= 1
        # 시간이 부족할 경우(음식을 다 못먹을 경우) 남은 음식 중에 먹어야 할 음식 찾기
        else:
            idx = k % food_num
            h.sort(key=lambda x: x[1])
            answer = h[idx][1]
            break

    return answer

# 처음에 푼 풀이
# 정확도 100 효율성 0 (문제점 : count와 find에서 시간초과)
# def solution(food_times, k):
#     answer = 0
#     food_cnt = len(food_times)
#     if sum(food_times) <= k:
#         return -1


#     cycle = 0
#     while k != 0:
#         food_cnt -= food_times.count(cycle)
#         cycle += 1
#         if food_cnt > k:
#             break
#         k -= food_cnt
#     answer = find(k+1, cycle, food_times)
#     return answer

# def find(number, cycle, food_times):
#     i = 0
#     while number != 0:
#         if food_times[i] < cycle:
#             i += 1
#             continue
#         number -= 1
#         i += 1
#     return i