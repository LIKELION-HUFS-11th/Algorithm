
from collections import deque

N = int(input())

# 처음 카드 -> N번 기술 -> 1~N

default_cards = deque() #처음 카드 -> 앞뒤에서 카드가 추가되므로 덱 사용!

tactics = list(map(int, input().split()))
tactics.reverse() #역순으로 봐야 하므로 reverse 정렬
# print(tactics)

cards = list(range(1, N+1, 1)) #[1, 2, ..., N-1, N] 최종 카드

for i in range(N):
    tactic = tactics[i]
    card = cards[i]

    if tactic == 1:
        default_cards.appendleft(card)
    
    elif tactic == 2:
        if i < 1:
            print("전략 2 실패")
            break
        
        first = default_cards.popleft()
        default_cards.appendleft(card)
        default_cards.appendleft(first)
    
    elif tactic == 3:
        if i < 1:
            print("전략 3 실패")
            break

        last = default_cards.append(card)

for elem in default_cards:
    print(elem, end=" ")

