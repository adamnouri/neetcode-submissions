class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        val = 0
        def dfs(i, j, pos):
            if pos == len(word):
                return True
            if min(i,j) < 0 or i >=  len(board) or j >= len(board[0]) or board[i][j] =="#" or board[i][j] != word[pos]:
                return False
        
            board[i][j] = "#"
            res = (dfs(i + 1, j, pos + 1) or dfs(i -1, j, pos + 1) or dfs(i , j + 1, pos + 1) or dfs(i, j - 1, pos + 1))
            board[i][j] = word[pos]
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False
        

            
            
            
        