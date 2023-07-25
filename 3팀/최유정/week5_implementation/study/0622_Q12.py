# build_frame의 원소 : [x, y, a, b] (x, y)좌표, a = 0(기둥) or 1(보), b = 0(삭제) or 1(설치)
# 5 <= n <= 100      1 <= build_fram <= 1000
# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

# 1. build_frame을 하나씩 돌면서 설치 또는 삭제가 가능한지 판단
# 1-1. b=1(설치)일 때 설치 조건에 따라 가능한지 확인
# 기둥 설치 조건 : y좌표가 0이거나 install 리스트 내에 [x-1, y, 1]이 있거나 [x, y, 1]이 있거나 [x, y-1, 0]이 있어야 함
# 보 설치 조건 : install 리스트 내에 [x, y-1, 0]이 있거나 [x+1, y-1, 0]이 있거나 ([x-1, y, 1] & [x+1, y, 1])이 있어야 함

# 1-2. b=0(삭제)일 때 우선 삭제시키고 남은 install에 있는 설치물들이 전부 설치조건에 맞는지 확인

#  XXXXXXXXXXXXXXXXXXX 조건이 너무 복잡 XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# 기둥 삭제 불가능한 조건(기둥 위쪽에 연결된 기둥 혹은 보가 있으면 안됨)
# 1. 위에 기둥이 있는데 보가 연결되어 있는 경우 삭제 가능 -> ([x, y+1, 0] in install and [x, y+1, 1] in install) or ([x, y+1, 0] in install and [x-1, y+1, 1] in install)
# 2. 위에 보가 연결되어 있을 때는 기둥을 삭제했을 때 설치조건에 충족하는지 확인
# 보 삭제 불가능 조건(보에 연결된 보가 기둥이 없으면 삭제가 불가능 보에 연결된 기둥에 아무것도 연결이 안되어 있으면 불가능)
#  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# 2. 설치 가능하면 install 리스트에 넣고, 삭제가 불가능하면 install 리스트에 다시 넣기

def can_install(x, y, a, install):
    if a == 0:
        if y == 0 or [x-1, y, 1] in install or [x, y-1, 0] in install or [x, y, 1] in install:
            return True
    else:
        if [x, y-1, 0] in install or [x+1, y-1, 0] in install or ([x-1, y, 1] in install and [x+1, y, 1] in install):
            return True
    return False

def valid(install):
    for x, y, a in install:
        if not can_install(x, y, a, install):
            return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1:
            if can_install(x, y, a, answer):
                answer.append([x, y, a])
        else:
            answer.remove([x, y, a])
            if not valid(answer):
                answer.append([x, y, a])
    answer.sort()
    return answer

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))