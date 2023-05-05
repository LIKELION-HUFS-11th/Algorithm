def solution(food_times, k):
    
    foods = []
    n = len(food_times)
    for i in range(n):
        foods.append((food_times[i], i+1))
    foods.sort()
    now = 0

    for i, food in enumerate(foods):
        diff = food[0] - now
        if diff:
            spend = diff * n
            if spend <= k:
                k -= spend
                now = food[0]
            else:
                k %= n
                temp = foods[i:]
                temp.sort(key=lambda x:x[1])
                return temp[k][1]

        n -= 1

    return -1