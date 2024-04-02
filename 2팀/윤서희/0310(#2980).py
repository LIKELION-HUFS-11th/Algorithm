import sys
input = sys.stdin.readline

n, l = map(int,input().split())   # 2 10

time = 0
place = 0

def caculate(d, r, g):
    global time, place
    time += (d - place)
    place = d
    if time % (r + g) <= r:
        time += (r - (time % (r + g)))

for i in range(n):
    d, r, g = map(int, input().split())  # 3 5 5, 5 2 2
    caculate(d, r, g)

time += (l - place)

print(time)


    
