"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        nMap = {node.val:Node(node.val)}
        
        dq = deque([node])
        
        while dq: 
            curr = dq.popleft()
            for neighbor in curr.neighbors:
                if neighbor.val not in nMap:
                    dq.append(neighbor)
                    nMap[neighbor.val] = Node(neighbor.val)
                nMap[curr.val].neighbors.append(nMap[neighbor.val])
                
                    
            
        return nMap[1]
                    

