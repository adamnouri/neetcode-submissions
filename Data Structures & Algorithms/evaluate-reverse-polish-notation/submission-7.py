import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
        }


        for el in tokens:
            if el not in operands:
                stack.append(int(el))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(operands[el](num2, num1))
                stack.append(res)
                
        return stack.pop()

            
                 

            
            
