class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.hq = nums
        self.size = k
        heapq.heapify(self.hq)
        while len(self.hq) > self.size:
            heapq.heappop(self.hq)
            


    def add(self, val: int) -> int:
        heapq.heappush(self.hq, val)
        while len(self.hq) > self.size:
            heapq.heappop(self.hq)
        return self.hq[0]

