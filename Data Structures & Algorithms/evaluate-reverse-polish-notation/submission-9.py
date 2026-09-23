class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i, tok in enumerate(tokens):
            if tok == "+":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                tok = num1 + num2
            elif tok == "-":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                tok = num2 - num1
            elif tok == "*":
                num1 = int(stack.pop())
                num2 = int(stack.pop())   
                tok = num2 * num1
            elif tok == "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                tok = num2 / num1
            stack.append(tok)
        
        return int(stack[-1])

                
