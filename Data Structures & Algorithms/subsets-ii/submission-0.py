class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        sub_array = []
        def dfs(index):
            if index >= len(nums):
                res.append(sub_array.copy())
                return
            sub_array.append(nums[index])
            dfs(index + 1)
            sub_array.pop()
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            dfs(index + 1)
        dfs(0)
        return res