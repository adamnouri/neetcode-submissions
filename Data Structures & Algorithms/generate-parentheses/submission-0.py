class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        subset = []
        res = []
        def dfs(opened, closed):
            if opened == closed == n:
                res.append("".join(subset))
                return
            if opened < n:
                subset.append("(")
                dfs(opened + 1, closed)
                subset.pop()
            if closed < opened:
                subset.append(")")
                dfs(opened, closed + 1)
                subset.pop()
            
        dfs(0,0)
        return res