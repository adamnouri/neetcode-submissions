# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        if not root:
            return []
        dq = deque([root])
        res = []
        size = 1
        while dq:            
            temp = []
            size = len(dq)
            for i in range(size):
                currNode = dq.popleft()
                if currNode:
                    temp.append(currNode.val)
                    dq.append(currNode.left)
                    dq.append(currNode.right)
            
            if temp:
                res.append(temp)
                
        return res
            
                

        