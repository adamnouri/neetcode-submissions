class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatBananas(x):
            
            hours = 0
            for n in piles:
                sol = n/x
                if sol == int(sol):
                    hours += sol
                else: 
                    hours += int(sol + 1)
            return hours <= h
        sol = max(piles)
        l, r = 1, max(piles)
        
        while l <= r:
            mid = l + (r - l)// 2
            if canEatBananas(mid):
                r = mid - 1
                sol = mid
            else:
                l = mid + 1
        return sol
