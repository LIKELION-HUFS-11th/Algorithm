class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_height = max(height)
        n = len(height)

        water = [0 for _ in range(n)]

        i = j = height.index(max_height)
        i -= 1
        j += 1

        while i > 0 or j < n-1:
            if i > 0:
                if height[i-1] > height[i]:
                    water[i] = height[i-1]
            if j < n-1:
                if height[j+1] > height[j]:
                    water[j] = height[j+1]
            i -= 1
            j += 1

            
        total = 0
        for i in range(n):
            water[i] = water[i] - height[i]
            if water[i] < 0:
                water[i] = 0
            
            total += water[i]
        print(water)

        return total
