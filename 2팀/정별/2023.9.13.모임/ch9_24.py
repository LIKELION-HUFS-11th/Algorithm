class MyQueue:

    def __init__(self):
        self.s1 = list()
        self.s2 = list()

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        put = self.s1[0]
        del self.s1[0]
        return put

    def peek(self) -> int:
        return self.s1[0]
        
    def empty(self) -> bool:
        return len(self.s1) == 0

obj = MyQueue()   
obj.push('a')
obj.push('b')
print(obj.peek())
print(obj.pop())
# print(obj.pop())
print(obj.empty())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()