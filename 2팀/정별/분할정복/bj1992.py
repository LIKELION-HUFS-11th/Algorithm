#참고링크: https://st-lab.tistory.com/230
import sys
# input = sys.stdin.readline()

n = int(input())
nList = list(list(input()) for _ in range(n))

# nVisited = [[0 for _ in range(n)] for _ in range(n)]
nAns = []

def check_possible(x, y, size): #x, y는 좌표상 전부 체크하는 포인터의 기준점임
    val = nList[x][y]
    for i in range(x, x + size): #x~x+size 만큼만 현위치의 1또는 0과 동일한지
        for j in range(y, y + size):
            if val != nList[i][j]:
                return False
    return True

def recursion(x, y, size):
    if check_possible(x, y, size): #범위 다 돌았는데 모두 같다면
        nAns.append(nList[x][y])
        return
    
    n_size = size//2
    nAns.append('(')
    #재귀 파트. 4방향 다 접근
    recursion(x, y, n_size) #좌상
    recursion(x, y+n_size, n_size) #우상
    recursion(x+n_size, y, n_size) #좌하
    recursion(x+n_size, y+n_size, n_size) #우하
    #안에서 다 돌고나서는 괄호 닫아주는 것임
    nAns.append(')')

recursion(0, 0, n)
print(''.join(nAns))




# def recursion(x, i, j, n):
#     if n == 1:
    
#     if x == '1':
#         nAns.append('1')
#         nVisited[i][j] = True
#         return
#     elif x == '0':
#         nAns.append('0')
#         nVisited[i][j] = True
#         return
    
#     nAns.append('(')
#     recursion(nList[][], , , n//2)
    
    