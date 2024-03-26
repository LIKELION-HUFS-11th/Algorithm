#예제는 맞게 나오는데, 계속 답이 틀렸다고 나옴.못풀음
#아 이렇게하면 10구할 때 5를, cnt 예외처리히야함.

n = int(input())
m = int(input())
nList = list(map(int, input().split()))

cnt = 0
for elem in nList:
    # if m/2 ==  float(m-elem):
    #     continue
    if m-elem in nList:
        cnt += 1
        nList[nList.index(m-elem)] = 0
       
        # nList.remove(m-elem) #모든 재료가 고유한 번호라서 가능. 중복됐다면 del로 제거

print(cnt)
#remove로 요소들이 삭제됨.
