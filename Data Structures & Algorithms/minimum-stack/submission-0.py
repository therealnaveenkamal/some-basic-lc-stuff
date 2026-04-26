class MinStack:

    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        if self.stack:
            prev_min = self.stack[-1][-1]
            self.stack.append([val, min(val, prev_min)])
        else:
            self.stack.append([val, val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][-1]
        
