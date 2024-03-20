from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.appendleft(x)
        
    def pop(self) -> int:
        return self.q.popleft()
        
    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q) == 0

stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.pop())
print(stack.empty())