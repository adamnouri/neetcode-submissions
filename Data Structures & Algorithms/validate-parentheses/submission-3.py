class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {"}":"{", ")" : "(" , "]":"["}
        stack = []
        for c in s:
            if c not in openToClose:
                stack.append(c)
            elif stack and stack[-1] == openToClose[c]:
                stack.pop()
            else:
                return False
             
        return True if not stack else False 



