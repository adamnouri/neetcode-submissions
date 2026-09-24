# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bfs(minVal, maxVal, node):
            if not node:
                return True
            if node.val >= maxVal or node.val <= minVal:
                return False
            
            return bfs(minVal, node.val,node.left) and bfs(node.val, maxVal, node.right)
        return bfs(float("-inf"), float("inf"), root)
                
        
