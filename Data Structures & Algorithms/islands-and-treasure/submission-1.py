class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()
        q = deque()
        dis = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append([r, c])
                    seen.add((r,c))
        def addCell(row, col):
            if min(row,col) < 0 or row >= len(grid) or col >= len(grid[0]) or (row, col) in seen or grid[row][col] == -1:
                return
            seen.add((row,col))
            q.append([row,col])
           
        
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dis
                addCell(row - 1, col)
                addCell(row + 1, col)
                addCell(row, col + 1)
                addCell(row, col - 1)
            dis += 1
           
            

            



            
                
        
        
        