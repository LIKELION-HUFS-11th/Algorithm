#string으로 입력받기!
n = input()


sum_1, sum_2=0,0

#럭키 스트레이트 사용할 수 있는 조건
for i in range (len(n)//2):
    sum_1 += int(n[i])

for j in range (len(n)//2,len(n)):
    sum_2 += int(n[j])

if sum_1 == sum_2:
    print("LUCKY")
    
else:
    print("READY")
