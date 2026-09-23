class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)
        def dfs(index, perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
            if index >= len(nums):
                return
            for i in range(len(nums)):
                if not pick[i]:
                    pick[i] = True
                    perm.append(nums[i])
                    dfs(index + 1, perm)
                    perm.pop()
                    pick[i] = False
        dfs(0, [])
        return res