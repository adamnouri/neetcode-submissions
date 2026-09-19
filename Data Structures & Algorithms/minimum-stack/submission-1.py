class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if not self.stack or self.minStack[-1] >= val:
            self.minStack.append(val)
            self.stack.append(val)
        else:
            self.stack.append(val)


    def pop(self) -> None:
        # Need to pop both if the top of stack is the same as minstack
        temp = self.stack.pop()
        if self.minStack[-1] == temp:
            return self.minStack.pop()
        return temp

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
