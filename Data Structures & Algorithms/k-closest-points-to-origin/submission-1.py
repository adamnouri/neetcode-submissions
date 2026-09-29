class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        x,y = 0, 0
        for point in points:
            x, y = point[0], point[1]
            dis = math.hypot(x,y)
            heapq.heappush(res, (-1 * dis, point))
            if len(res) > k: 
                heapq.heappop(res)
        
        return [point for dis, point in res]
