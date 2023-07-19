# 자물쇠와 열쇠
from copy import deepcopy

# 1번째 풀이
def rotated(key):
    new_key = [[0 for y in range(len(key))] for x in range(len(key))]
    for x in range(len(key)):
        for y in range(len(key)):
            new_key[x][y] = key[y][abs(x-(len(key)-1))]
    return new_key


def check(ano_lock):
    n = len(ano_lock) // 3
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if ano_lock[i][j] != 1:
                return False
    return True


def solution1(key, lock):
    m, n = len(key), len(lock)
    new_lock = [[0]* (3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]
    for _ in range(4):
        key = rotated(key)
        for x in range(1, 2*n):
            for y in range(1, 2*n):
                for i in range(m):
                    for j in range(m):
                        new_lock[i+x][j+y] += key[i][j]
                if check(new_lock):
                    return True
                else:
                    for i in range(m):
                        for j in range(m):
                            new_lock[i+x][j+y] -= key[i][j]
    return False


# 2번째 풀이
def extending(lock, M):
    new_lock = [[0]*(3*M-2) for _ in range(3*M-2)]
    zero_location = []
    for i in range(M):
        for j in range(M):
            if lock[i][j] == 0:
                zero_location.append([i, j])
            new_lock[i+(M-1)][j+(M-1)] = lock[i][j]
    return new_lock, zero_location

def check(check_lock, key, x, y, N):
    for i in range(N):
        for j in range(N):
            check_lock[x+i][y+j] += key[i][j]
            if check_lock[x+i][y+j] == 2:
                return False
    return True

def open_lock(check_lock, zero_location, M):
    for i, j in zero_location:
        if check_lock[i+M-1][j+M-1] != 1:
            return False
    return True

def rotate(key, N):
    new_key = deepcopy(key)
    for i in range(N):
        for j in range(N):
            new_key[i][j] = key[N-j-1][i]
    return new_key



def solution2(key, lock):
    M = len(lock)
    N = len(key)
    new_lock, zero_location = extending(lock, M)
    if zero_location == []:
        return True

    for x in range(2*M-1):
        for y in range(2*M-1):
            for _ in range(4):
                key = rotate(key, N)
                check_lock = deepcopy(new_lock)
                if check(check_lock, key, x, y, N):
                    if open_lock(check_lock, zero_location, M):
                        return True
    return False