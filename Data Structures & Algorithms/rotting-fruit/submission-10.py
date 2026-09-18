from collections import deque 
class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        dq = deque()
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    dq.append((r,c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and dq:
            for _ in range(len(dq)):
                r, c = dq.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
                        grid[row][col] = 2
                        
                        dq.append((row,col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1




            
                
            

                    


