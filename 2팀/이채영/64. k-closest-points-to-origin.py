import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # 가장 가까운 점 k개

        heap = []
        dict = {}

        for i in range(len(points)):
            x, y = points[i]
            distance = (x**2) + (y**2)

            if distance in dict:
                dict[distance].append([x, y])
            else:
                dict[distance] = [[x, y]] #2차원 리스트

            heapq.heappush(heap, distance)
        # print(dict)

        result = []
        for i in range(k):
            elem = heapq.heappop(heap) #distance
            result.append(dict[elem][0])
            del dict[elem][0]

        return result
