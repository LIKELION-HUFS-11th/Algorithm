def touched(pos, lock):
    n = len(lock)
    x, y = pos[0], pos[1]
    
    return (0<= x < n and 0 <= y < n) and lock[x][y]
    
    
def check(key_pos, i, j, lock_pos, lock):
    curr_key_pos = []
    
    for pos in key_pos:
        curr_key_pos.append([pos[0] + i, pos[1] + j])
    
    # 다 찼는지 확인
    for pos in lock_pos:
        if pos not in curr_key_pos:
            return False
    
    # 튀어나온 부분끼리 닿았는지 확인
    for pos in curr_key_pos:
        # 채운 거 제외, 범위 내에서 lock에서 튀어나왔는지
        if (pos not in lock_pos) and touched(pos, lock):
            return False
    
    return True

def circulate(m, key):
    
    new_key = [
        [0] * m
        for _ in range(m)
    ]
    
    a, b = m-1, 0
    for i in range(m):
        for j in range(m):
            new_key[i][j] = key[a][b]
            a -= 1
        a = m-1
        b += 1
    
    return new_key

def simulate(dir, m, n, key, lock):
    # dir만큼 회전시키기
    for _ in range(dir):
        key = circulate(m, key)
    
    # 열쇠가 나와 있는 위치, 락커에서 빈 위치
    key_pos, lock_pos = [], []
    
    for i in range(m):
        for j in range(m):
            if key[i][j]:
                key_pos.append([i, j])
    for i in range(n):
        for j in range(n):
            if not lock[i][j]:
                lock_pos.append([i, j])
    
    # -n, -n에서 n, n까지 움직이면서
    for i in range(-(n*2), n*2):
        for j in range(-(n*2), n*2):
            # 체크를 통과하면
            if check(key_pos, i, j, lock_pos, lock):
                # 성공
                return True
    
    return False

def solution(key, lock):
    m, n = len(key), len(lock)
    
    # key를 시계방향으로 회전시켜가면서
    for i in range(4):
        # 시뮬레이션 한번이라도 성공하면
        if simulate(i, m, n, key, lock):
            # 성공
            return True
        
    return False 