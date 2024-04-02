

S= input()

sList=[]
sSet = {}

size = 1 #도는 포인터의 크기

while size <= len(S):
    for i in range(0, len(S)):
        sList.append(S[i:i+size])
    size+=1
# print(set(sList))
print(len(set(sList)))   