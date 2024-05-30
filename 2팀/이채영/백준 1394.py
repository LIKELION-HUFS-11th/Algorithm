import sys
input = sys.stdin.readline


def decode(n, total):
    global len_all, len_key, strs


    c = key[n] #현재 보고 있는 문자

    before = strs.index(c) #c 이전에 있는 문자 개수

    if n == len_key - 1:
        total += (before + 1)

        return total


    cnt = (len_all ** (len_key-n-1)) * before #b - -, c - -를 뽑는 경우의 수 

    return decode(n+1, total + cnt)



strs = list(input().strip())
key = list(input().strip())

len_all = len(strs)
len_key = len(key)

result = 0
for i in range(1, len_key): #1~n-1개 뽑는 경우 처리
    result += len_all ** i


middle = decode(0, 0) #n개 뽑는 경우 처리 


result += middle

print(result % 900528)