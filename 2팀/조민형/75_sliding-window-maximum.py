from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 결과를 저장할 리스트
        result = []
        # 윈도우 내에서 최댓값 후보들의 인덱스를 저장할 덱 초기화
        deq = deque()
        
        for i in range(len(nums)):
            # 새로운 요소를 추가하기 전에, 덱의 뒤에서 현재 요소보다 작은 모든 요소를 제거
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
                
            # 새 요소의 인덱스를 덱의 뒤에 추가
            deq.append(i)
            
            # 덱의 앞쪽에 있는 요소가 윈도우 범위를 벗어났다면 제거
            if deq[0] == i - k:
                deq.popleft()
            
            # 윈도우의 크기가 k가 되면, 덱의 첫 번째 요소(현재 윈도우의 최댓값)를 결과에 추가
            if i >= k - 1:
                result.append(nums[deq[0]])
        
        return result


# O(nklogn)
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         result = []
#         for i in range(len(nums)-k+1):
#             tempList = nums[i:i+k]
#             if k == 1:
#                 result.append(tempList[0])
#             #k가 2 이상일 때
#             elif i == 0:
#                 sortedNums = sorted(tempList)
#                 maxNum = sortedNums[-1]
#                 secMaxNum = sortedNums[-2]
#                 result.append(maxNum)
#             else:
#                 # 빠진 수가 최댓값이었을 경우(최댓값과 두번째로 큰 값 업데이트 필요)
#                 if nums[i-1] == maxNum:
#                     #들어온 수가 과거 최댓값보다 작지만 두 번째 큰 수보다는 클 때
#                     if secMaxNum < tempList[-1]:
#                         # 이것도 새로 들어온 값이 최댓값으로 업데이트되기 때문에 두번째 큰 값은 변동 x
#                         maxNum = tempList[-1]
#                         result.append(maxNum)
#                     # 들어온 수가 과거 최댓값과 두번째 큰 수보다 작을 때
#                     else:
#                         #두번째 큰 수가 최댓값이 됨
#                         sortedNums = sorted(tempList)
#                         maxNum = sortedNums[-1]
#                         secMaxNum = sortedNums[-2]
#                         result.append(maxNum)
                        
#                 # 빠진 수가 최댓값이 아니었을 경우
#                 else:
#                     # 최댓값보다 새로 들어온 값이 클 경우
#                     if maxNum < tempList[-1]:
#                         # 최댓값이 밀려 두번째로 큰 값이 됨
#                         secMaxNum = maxNum
#                         # 최댓값을 새로 들어온 값으로 업데이트
#                         maxNum = tempList[-1]
#                         result.append(maxNum)
#                     # 최댓값보다 새로 들어온 값이 작을 경우
#                     else:
#                         #두번째로 큰 값보다 새로 들어온 값이 클 경우
#                         if secMaxNum < tempList[-1]:
#                             #두번째로 큰 값 없데이트
#                             secMaxNum = tempList[-1]
#                         #두번째로 큰 값보다 새로 들어온 값이 작은 경우는 어떤 값도 업데이트가 필요 없으므로 넘김
#                         result.append(maxNum)
#         return result