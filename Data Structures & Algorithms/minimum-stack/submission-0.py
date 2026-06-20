class MinStack:

    def __init__(self):
         self.minStack = []
         self.normStack = []

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append(val)
        elif val <= self.minStack[-1]:
            self.minStack.append(val)
        self.normStack.append(val)

    def pop(self) -> None:
        if self.minStack[-1] == self.normStack[-1]:
            self.minStack.pop()
        self.normStack.pop()

    def top(self) -> int:
        return self.normStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
