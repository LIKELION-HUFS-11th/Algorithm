#모르겠다 해결하기

import sys
input = sys.stdin.readline

global n, w, l

def crooss_bridge(time, weight, next):
    global n, w, l

    if weight + trucks_weight[next] > l: #진입 안됨
        for t in on_bridge:
            trucks_time[t]
        

    

n, w, l = tuple(map(int, input().split()))

trucks_weight = list(map(int, input().split()))
trucks_time = [w+1 for _ in range(len(trucks_weight))] #남은 길이

# blank = [0 for _ in range(w)]

on_bridge = [0] #0번트럭 올라갈 예정
crooss_bridge(1, trucks_weight[0], 1)