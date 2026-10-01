class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        return not len(nums) == len(seen)