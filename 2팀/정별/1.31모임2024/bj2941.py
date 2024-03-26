strW = input()

dict = ['c=',
'c-',
'dz=',
'd-',
'ni',
's=',
'z=']

cnt = 0

for i in range(len(dict)):
    cnt += strW.count(dict[i])
    while strW.count(dict[i]) > 0:
        strW.remove(dict[i])
    # strW.index(dict[i])
    

    if i == len(dict)-1: #다 돌고나서
        cnt += len(strW)
        
print(cnt)