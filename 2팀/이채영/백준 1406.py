# 테케는 다 맞았는데 시간초과뜸

import sys
input = sys.stdin.readline

global string, cursor

def P(s):
    global string, cursor

   
    string.insert(cursor, s)
    cursor += 1

def L():
    global string, cursor
  
    if cursor == 0:
        return
    cursor -= 1

def D():
    global string, cursor
  
    if cursor == len(string):
        return
    cursor += 1

def B():
    global string, cursor

    if cursor == 0:
        return
    del string[cursor-1]
    cursor -= 1



string = input().strip()
string = list(string)
cursor = len(string) #[a, b, c, d, -]

m = int(input().strip())

for _ in range(m):
    order = input().strip()

    if len(order) > 1:
        order, s = order.split()

    if order == 'P':
        P(s)
    elif order == 'L':
        L()
    elif order == 'D':
        D()
    elif order == 'B':
        B()

    # print(string)
    
print("".join(string))
