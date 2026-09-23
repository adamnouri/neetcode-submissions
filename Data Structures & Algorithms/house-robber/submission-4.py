class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        def bfs(index):
            if index == n:
                dp[n] = max(dp[index - 2], dp[index - 1])
                return
            if index < 2:
                dp[index] = nums[index]
            elif index - 3 <0:
                dp[index] = nums[index] + dp[index - 2]
            else:
                dp[index] = nums[index] + max(dp[index - 3], dp[index-2])
            bfs(index + 1)
                
        bfs(0)
        return dp[n]

