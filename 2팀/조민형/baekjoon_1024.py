import sys
input = sys.stdin.readline

n,l = map(int,input().split())

result = -1

for i in range(l,101): #L이  100보다 같거나 같은 자연수
    j = 0.5*(2*n/i - i+1) # 등차수열의 합 이항정리로 시작점의 값 찾기
    if j.is_integer(): # j가 정수여야 성립하기 때문에 조건
        result = [k for k in range(int(j),int(j+i))]
        if -1 in result: # 성립이 불가능한 조건 -> 재할당이 안 되었을 때
            result = -1
            continue
        break
    

if result == -1:
    print(result)
else:
    for i in result:
        print(i,end=' ')
    print()