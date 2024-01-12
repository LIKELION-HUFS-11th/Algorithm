class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 0은 제일 앞으로, 2는 제일 뒤로

        #quick sort
        #Sol1
        # S = []
        # M = []
        # L = []

        # for elem in nums:
        #     if elem == 0:
        #         S.append(elem)
        #     elif elem == 1:
        #         M.append(elem)
        #     else:
        #         L.append(elem)

        # nums = S + M + L

        #Sol2
        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1