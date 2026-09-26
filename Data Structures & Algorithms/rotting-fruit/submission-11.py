class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0
        ROW, COL = len(grid), len(grid[0])
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [[-1, 0], [1, 0], [0,-1], [0,1]]
        while q and fresh:
            
            length = len(q)
            for _ in range(length):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row+ dr, col + dc
                    if (r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == 1):
                        grid[r][c] = 2
                        q.append((r,c))
                        fresh -=1
            time += 1
        return time if fresh == 0 else -1
                    
            
                
                    
                    
            