n = int(input())
inp_list=[]
pointer = 0
for _ in range(n):
    elem = int(input())
    if elem > pointer:
        inp_list.append(elem)
        pointer = elem #5


inp_list = [list(map(int, (input().split('\n')))) for _ in range(n)]

ans_list =[]
pointer= 0
for elem in inp_list:
    if elem[0] > pointer:
        
        
        
# 구글링한 답
# import sys
# input=sys.stdin.readline

# n=int(input())
# li=[]

# for i in range(n):
#     li.append(int(input()))

# for i in sorted(li):
#     print(i)