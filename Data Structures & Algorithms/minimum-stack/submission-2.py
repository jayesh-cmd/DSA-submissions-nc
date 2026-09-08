class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = []

    def push(self, val: int) -> None:

        self.stack.append(val)

        if not self.minn:
            self.minn.append(val)
        else:
            curr = self.minn[-1]
            self.minn.append(min(curr, val))

    def pop(self) -> None:
        self.minn.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minn[-1]