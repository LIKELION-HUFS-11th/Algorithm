from typing import List
#풀이1. 977ms
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_diff = 0  # 전체 차이 계산
        current_diff = 0  # 현재까지의 차이
        start_idx = 0  # 출발점 후보지

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_diff += diff
            current_diff += diff

            if current_diff < 0:
                # 현재까지의 차이가 음수인 경우 현재 위치를 출발점으로 지정
                current_diff = 0
                start_idx = i + 1

        # 출발 지점을 찾을 수 없는 경우 또는 전체 차이가 음수인 경우 -1 반환
        return start_idx if total_diff >= 0 else -1
    

#풀이2. 런타임 에러. 처음에 짠 코드
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dif = [] #이동 직후 각 인덱스마다 발생하는 비용+충전량
        for g, c in zip(gas, cost):
            dif.append(g-c)


        if sum(dif) >= 0:
            idx_list = [] #출발점 후보지들의 인덱스값 저장 리스트
            for elem in dif:
                if elem > 0: #가능한 출발점 먼저 찾기
                    idx_list.append(dif.index(elem))

            for idx in idx_list: #차이 나는 것들에서 양수만 뽑았으니, 시간복잡도 적을지도..?
                pointer = 0 #원형으로 돌 수 있게 해줌. 총 리스트 안을 돌린 횟수
                cnt = 0 #기름 잔여량
                while True:
                    cnt += dif[idx] #기름 잔여량 갱신
                    idx += 1
                    if idx == len(dif):
                        idx = 0 #dif 리스트의 처음으로 돌아가서 반복 돌리기

                    if cnt < 0 : #음수라는건, 기름이 다 떨어졌다는 뜻
                        cnt = 0 #다시 0으로 초기화
                        pointer = 0 #다시 dif 돌기 시작 위해.
                        break #idx 후보 탈락, 다음 후보로 넘어감.
                    
                    pointer += 1
                    if pointer == len(dif): #dif를 전부 돌았으면 종료
                        return idx                
        else:
            return -1  



