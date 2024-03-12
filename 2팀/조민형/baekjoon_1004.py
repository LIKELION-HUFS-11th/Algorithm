import sys

# 시작점 혹은 도착점이 원 안에 들어있는지 확인
def in_circle(x,y,r,temp_x,temp_y):
    if r**2 > (( x - temp_x)**2) + ((y - temp_y)**2):
        return True
    else: return False

# 테스트 케이스
T = int(sys.stdin.readline())



result_print = []
#테스트 케이스 동안
for i in range(T):
    #시작점, 도착점
    start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())
    # 행성 개수 받기
    planet = int(sys.stdin.readline())
    # 행성 개수만큼 행성 좌표 받기
    result = 0
    for j in range(planet):
        planet_x, planet_y, r = map(int,sys.stdin.readline().split())
        # 출발점과 도착점이 원 안에 있을 경우만 생각
        if in_circle(planet_x,planet_y,r,start_x,start_y) and in_circle(planet_x,planet_y,r,end_x,end_y):
            pass
        elif in_circle(planet_x,planet_y,r,start_x,start_y):
            result += 1
        elif in_circle(planet_x,planet_y,r,end_x,end_y):
            result += 1
    result_print.append(result)

for k in result_print:
    print(k)


    