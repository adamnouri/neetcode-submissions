class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        

        for i in range(len(temperatures) - 1):
            stack.append((temperatures[i], i))
            if temperatures[i + 1] > temperatures[i]:
                while stack and stack[-1][0] < temperatures[i + 1]:
                    index = stack.pop()[1]
                    res[index] = i - index + 1
            
            




        return res
            
             