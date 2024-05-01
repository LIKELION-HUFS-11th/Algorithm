import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #5C3

top, bottom = 1, 1

for i in range(n, n - m, -1): #(5, 2)
    top *= i


for i in range(m, 0, -1):
    bottom *= i
    

print(top // bottom)