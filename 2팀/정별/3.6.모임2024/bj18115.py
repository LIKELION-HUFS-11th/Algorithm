def find_initial_cards(N, A):
    initial_cards = [0] * N  

    current_card = N  # 처음 카드의 번호는 N부터 시작
    for i in range(N-1, -1, -1):  # 뒤에서부터 순회하면서
        if A[i] == 1:  # 1번 기술을 사용했을 때
            initial_cards[i] = current_card  # 현재 카드를 i번째 위치에 놓음
            
            current_card -= 1  # 다음 카드의 번호는 하나 줄어듦
            
        elif A[i] == 2:  # 2번 기술을 사용했을 때
            initial_cards[i] = initial_cards[i+1]  # 오른쪽에 있는 카드를 i번째 위치에 놓음
        else:  # 3번 기술을 사용했을 때
            initial_cards[i] = initial_cards[-1]  # 가장 마지막 카드를 i번째 위치에 놓음

    return initial_cards

N = int(input())
A = list(map(int, input().split()))

initial_cards = find_initial_cards(N, A)

# 초기 카드의 상태를 출력합니다.
print(*initial_cards)
