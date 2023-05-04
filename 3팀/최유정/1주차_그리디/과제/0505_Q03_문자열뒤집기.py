S = input()
s_list = list(map(int, S))
cnt = 0


for i in range(len(s_list)-1):
    if s_list[i] != s_list[i+1]:
        cnt += 1

print((cnt+1)//2)