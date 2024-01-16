
n = int(input())
inp = [list(input().split()) for _ in range(n)]

order = 0    
for elem in inp:
    elem[0] = int(elem[0])
    elem.append(order)
    order+=1


sorted_inp = sorted(inp, key = lambda x : (x[0], x[2]))

for elem in sorted_inp:
    print(elem[0], elem[1]) 