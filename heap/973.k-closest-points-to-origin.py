import math

from heapq import heappush, heappop, heapify

class Solution:
    class Point:

        def __init__(self, x, y) -> None:
            self.x = x
            self.y = y
            self.distance = self.cal_distance()
        
        def __lt__(self, other):
            return self.distance < other.distance
        
        def cal_distance(self):
            square_sum = math.pow((self.x - 0), 2) + math.pow((self.y-0), 2)
            return math.sqrt(square_sum)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            p = Solution.Point(x=point[0], y=point[1])
            heappush(heap, p)
        closest_points = []
        for _ in range(k):
            p = heappop(heap)
            closest_points.append([p.x, p.y])
        return closest_points