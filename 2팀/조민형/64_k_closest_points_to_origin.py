class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        new_points = []
        for (x,y) in points:
            dist = math.sqrt(x**2 + y**2)
            new_points.append([[x,y],dist])

        new_points.sort(key = lambda x : x[1])
        
        result_points = []
        for i in range(k):
            result_points.append(new_points[i][0])

        return result_points