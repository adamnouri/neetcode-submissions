class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums) 
        maxCount = 0
        
        for n in seq: 
            if (n - 1) not in seq:
                currCount = 1
                while n+currCount in seq:
                    currCount += 1
                    maxCount = max(currCount, maxCount)
                maxCount = max(currCount, maxCount)
        return maxCount

