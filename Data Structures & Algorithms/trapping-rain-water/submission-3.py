class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    right, left = height[i], height[stack[-1]]
                    w = i - stack[-1] - 1
                    h = min(left,right) - mid
                    res += h*w
            stack.append(i)
        return res


