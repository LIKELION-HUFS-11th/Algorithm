import math, heapq, heap
class Solution:
    def kClosest(self, points, k: int) :
        for (x, y) in points:
            dist = math.sqrt((0-x)**2 + (0-y)**2)
            heapq.heappush(heap, (dist, x, y))
            
        res = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            res.append(x,y)
        return res