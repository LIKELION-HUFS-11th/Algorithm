n = int(input())
dis = list(map(int, input().split()))
L = list(map(int, input().split()))
c_list = []
total = 0

total_dis = sum(dis)
for i in range(n-1):
    c_list.append([L[i], total_dis])
    total_dis -= dis[i]

c_list.sort()
total_dis = sum(dis)
dis_sum = 0

for c in c_list:
    c[1]  -= dis_sum
    if total_dis == 0:
        break
    if c[1] > 0:
        total += c[0] * c[1]
        total_dis -= c[1]
        dis_sum += c[1]
print(total)