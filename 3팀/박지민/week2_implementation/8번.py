s = input()

result = []
sum = 0
for i in s:
    #알파벳이라면 result에 추가, 오름차순 정렬
    if i.isalpha():
        result.append(i)
    #숫자라면    
    else:
        sum += int(i)
#알파벳 오름차순 정렬    
result.sort()

if sum != 0:
    result.append(str(sum))    

for i in result:
    print(i,end='')