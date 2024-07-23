import sys

k = int(input())

sList = sys.stdin.readline().split()
# print(sList)

def check(i, j, sign):
    if sign == '<':
        return i < j
    else: #sign이 >
        return i > j

nVisited =[0 for _ in range(10)]
nums =[]
# Ans = []
max_ans, min_ans = "", ""

# def BT(idx, nums,  nVisited, sList):
#     #인자들: 현재위치, 지금까지 선택된 숫자리스트, 숫자 사용여부, 부등호 리스트

def BT(idx, s):
    global max_ans, min_ans

    if idx == k+1:
        if not min_ans: #for문으로 앞자리부터순서대로 0->9까지 돌으니까 첫번째 경우가 가장 작은수
            min_ans = s
        else:
            max_ans = s
        # Ans.append("".join(map(str, nums))) #문자열로 바꿔서 추가
        return
    
    for i in range(10): #0~9까지 시도
        if not nVisited[i]:#이미 사용했으면 패스. 각 숫자는 한번만 쓸 수 있음
            #가장 첫번째 숫자이거나
                #바로 직전 숫자랑 부등호 관계가 참일 때
            if idx == 0 or (check(s[-1], str(i), sList[idx-1]) == True):
                nVisited[i] =True
                # nums.append(i)

                #여기서 재귀 호출해서 다음 선택
                BT(idx+1, s+str(i)) #뒤에 숫자들도 계속 추가해줌.
                
                #이 작업 안해주면 nums랑 nVisited 계속 중복됨
                # nums.pop()
                nVisited[i] =False

BT(0, "") #아예 빈칸의 문자열에서 시작
print(max_ans)
print(min_ans)  
                

        
        
        
