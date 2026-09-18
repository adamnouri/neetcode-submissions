class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        def traversal(grid, i, j): 
            if i < 0 or i >= len(grid) or j<0 or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0 
            else:
                grid[i][j] = 0
                res = 1 + traversal(grid, i - 1, j) + traversal(grid, i, j - 1) + traversal(grid, i + 1, j) + traversal(grid, i, j + 1)
                return res
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: 
                    maxArea = max(maxArea, traversal(grid, i, j))
        return maxArea
                


        