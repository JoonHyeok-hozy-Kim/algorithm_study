class MinStack:

    def __init__(self):
        self.s = []
        self.m = []        
        
    
    def is_empty(self):
        return len(self.s) == 0
    

    def push(self, val: int) -> None:
        if self.is_empty():
            self.m.append(val)
        else:
            self.m.append(min(self.m[-1], val))
        self.s.append(val)
        

    def pop(self) -> None:
        # if self.is_empty:
        #     raise Exception()
        self.s.pop()
        self.m.pop()
        

    def top(self) -> int:
        # if self.is_empty():
        #     raise Exception()
        return self.s[-1]
        

    def getMin(self) -> int:
        # if self.is_empty():
        #     raise Exception()
        return self.m[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()