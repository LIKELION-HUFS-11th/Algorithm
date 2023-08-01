#입력
import sys
#n = 카드 묶음 개수
n = int(input())
# cards_len = 카드 묶음 각각의 크기
cards_len=[]
input = sys.stdin.readLine()
cards_len.append(input)
#설계

#정렬 -> 두 개씩 더하기
cards_len.sort()
#
cnt =0
#2개씩 
for i in range(n-1):
    cnt += cards_len[i]

    if len(cards_len) == 1:
        cnt += 
        break
    
#출력