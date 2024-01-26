class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Counter 모듈 사용
        from collections import Counter

        # 필요한 값에 대해 Counter를 통해 딕셔너리로 만듦. 각 문자와 그 문자의 개수가 딕셔너리로 나옴
        need = Counter(t)
        # 필요한 문자의 전체 개수
        missing = len(t)
        #포인터 지정
        left = start= end = 0

        #right가 1부터 시작
        for right, char in enumerate(s,1):
            # 필요한 개수에서 만약 해당 문자가 필요한 값에 있는지 찾고 만약 필요하다면 필요한 문자의 전체 개수 -1, 아니면 아무것도 뺴지 않음
            missing -=need[char]>0
            # 필요한 값에서 하나를 지웠으므로 딕셔너리의 값도 업데이트
            need[char]-=1

            # 필요한 문자의 전체 개수가 0이 되었을 때(모든 문자가 해당 문자열 안에 들어가 있을 때) -> 줄일 가능성이 있나 찾아봐야함
            if missing ==0:
                #왼쪽 포인터가 가르키는 값이 필요없는 값일 경우 -> need 딕셔너리에서 음수를 가지고 있음
                while left < right and need[s[left]] <0:
                    #왼쪽으로 포인터를 이동하면서 해당 딕셔너리와 포인터에 1씩 더해줌
                    need[s[left]] +=1
                    left +=1
                
                #필요한 값을 삭제하고 더 길이를 줄일 여지가 있는지 확인(윈도우의 크기)과 함께 전에 만족했던 문자열과의 길이도 비교
                if not end or right - left <= end-start:
                    #해당 인덱스 값을 저장해놓음
                    start,end = left,right
                    #왼쪽 필요한 값과 필요한 문자의 수 1개씩 더해주면서 더 줄일 가능성도 찾음
                    need[s[left]] +=1
                    missing +=1
                    left +=1

        # 저장해놨던 인덱스 값을 리턴
        return s[start:end]



# from collections import Counter

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         def check_letter(s, t):
#             s_dict = Counter(s)
#             # t의 모든 문자가 s에 포함되어 있는지 확인
#             for char in t:
#                 if s_dict[char] - t_dict[char] < 0:
#                     return False
#             return True
        
#         t_dict = Counter(t)
#         i = len(t)-1
#         j=0
#         result = ""
    
#          # 필요한 수와 총 문자의 길이가 같고 정렬해봤을떄 같으면 -> 바로 s 리턴
#         if len(t)==len(s) and sorted(s) == sorted(t):
#             return s
#          # 필요한 문자열이 한개밖에 없으면 -> 하나만 in으로 찾은 뒤 바로 리턴
#         elif len(t)==1 and t in s:
#             return t
#          # 필요한 문자열이 전체 문자열보다 길 경우 -> 어차피 성립이 안되므로 빈 문자열 리턴
#         elif len(t)>len(s):
#             return ""
#         # 조건을 다 지나고 난 뒤에 나머지 조건들의 경우
#         while i<=len(s):
#              #i가 맨 끝에 도달할 때까지 반복하면서 해당 문자열과 찾는 문자열을 check_letter에 돌린 뒤 참이 나오면
#             if check_letter(s[j:i],t_dict) == True:
#                 # 결과가 만약에 저장되어 있는 상태 -> 길이 비교 후 더 작으면 결과도 없데이트
#                 if result and len(result) > len(s[j:i]):
#                     result = s[j:i]
#                     j+=1
#                     continue
#                  # 아니라면 그냥 왼쪽 포인터만 오른쪽으로 옮김
#                 elif result:
#                     j+=1
#                     continue
#                 # 문자열을 아직 한 번도 못찾았을 때 쓰이는 조건
#                 result = s[j:i]
#                 j+=1
#              #조건을 통과하지 못함 -> 다시 오른쪽으로 포인터를 옮겨서 찾아봐야 함
#             else:
#                 i+=1
#          # 결과가 저장되어 있을 경우
#         if result:
#             return result
#          # 결과가 저장되어 있지 않을 경우 -> 빈 문자열 리턴
#         else: return ""
    