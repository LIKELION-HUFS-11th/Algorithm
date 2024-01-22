class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = nums.index(min(nums))
        left,right = 0, len(nums) -1
        
        while left <= right:
            #완벽한 mid 구하기 -> left+right//2보다 오휴발생률이 적음
            mid = left + (right-left) //2
            #피봇 위치 -> pivot만큼 회전했으므로 mid에 피봇의 index만큼 추가로 더하기
            mid_pivot = (mid + pivot) % len(nums)

            #기존과 똑같이 움직이되 어차피 left, right가 달라지면 mid와 mid_pivot또한 달라지므로 회전된 상태에서의 이진 탐색이 가능
            if nums[mid_pivot] < target:
                left = mid+1
            elif nums[mid_pivot] > target:
                right = mid -1
            else:
                return mid_pivot
        return -1
        