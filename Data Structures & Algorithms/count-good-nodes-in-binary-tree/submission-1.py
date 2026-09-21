# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # BFS
        currMax =float('-inf')
        ans = 0
        q = deque([(currMax, root)])
        while q:
            for i in range(len(q)):
                currMax, currNode = q.popleft()
                if currNode.val >= currMax:
                    ans += 1
                currMax = max(currMax, currNode.val)
                if currNode.left:
                    q.append((currMax, currNode.left))
                if currNode.right:
                    q.append((currMax, currNode.right))
            
        return ans

               

            

