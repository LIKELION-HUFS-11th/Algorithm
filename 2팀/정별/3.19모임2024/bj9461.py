import sys
n = int(sys.stdin.readline().strip())

nList =[1,1,1]

for i in range(3, 100):
    nList.append(nList[i-2] + nList[i-3])


for _ in range(n):
    N = int(sys.stdin.readline().strip())

    print(nList[N-1])




# def pado(k):
#     if k <= 3:
#         return 1
#     elif k <= 5:
#         return 2
    
#     return pado(k-5) + pado(k-1)

# nList =[int(sys.stdin.readline().strip()) for _ in range(n)]


# for elem in nList:
#     print(pado(elem))


