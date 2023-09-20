class MyQueue:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.empty():
            self.items.pop(0)

    def peek(self):
        if not self.empty():
            return self.items[0]
        
queue = MyQueue()

queue.push(1)
print(queue.items)
queue.push(2)
print(queue.items)
queue.peek()
queue.pop()
print(queue.items)
queue.empty()
