class MyQueue:

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        self.peek()
        return self.b.pop()

    def peek(self) -> int:
        if len(self.b) == 0:
            while len(self.a):
                self.b.append(self.a.pop())
        return self.b[-1]

    def empty(self) -> bool:
        if len(self.a) == 0 and len(self.b) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
