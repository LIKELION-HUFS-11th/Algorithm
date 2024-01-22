n, k = map(int, input().split())
knap_dict = dict()
for _ in range(n):
    w, v = map(int, input().split())
    knap_dict[(w, v)] = v / w

sorted_dict = sorted(knap_dict.items(), key=lambda x: x[1], reverse=True)
sorted_wv = [x[0] for x in sorted_dict]

max_value = 0
def frac_knapsack(idx, weight):
    global max_value

    if weight == 0 or idx == n:
        return max_value
    
    if weight >= sorted_dict[idx]:
        max_value += sorted_dict[idx][0][1]
        weight -= sorted_dict[idx][0][0]
        frac_knapsack(idx + 1, weight)
    else:
        max_value += sorted_dict[idx][1] * weight
        frac_knapsack(idx + 1, 0)

def sum_values(s, e):
    values = 0
    for i in range(s, e):
        values += sorted_wv[i][1]
    return values

max_sum = 0
def knapsack(idx, weight):
    if idx >= n or weight <= 0:
        return max_sum

    if sorted_wv[idx][0] <= weight:
        # if sum_values(0, idx) + sorted_wv[idx][1] +  > max_sum:
        pass
