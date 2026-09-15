class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.traversal(i, j, grid)
                    grid[i][j] = "0"
                    res += 1

        return res
    def traversal(self, i, j, grid):
        if i == len(grid) or j == len(grid[0]) or j < 0 or i < 0:
            return
        elif grid[i][j] == "0":
            return
        else: 
            grid[i][j] = "0"
            self.traversal(i + 1, j, grid)
            self.traversal(i, j+1, grid)
            self.traversal(i- 1, j, grid)
            self.traversal(i, j-1, grid)
            


        
            