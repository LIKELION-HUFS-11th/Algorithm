# 럭키스트레이트

N = input()
n_list = list(map(int, N))
c = len(n_list)//2

if sum(n_list[:c])==sum(n_list[c:]):
    print("LUCKY")
else:
    print("READY")