from collections import deque


class MyQueue:

    def __init__(self, dq = deque()):
        self.dq = deque() if not dq else dq

    def push(self, x: int) -> None:
        self.dq.appendleft(x)              

    def pop(self) -> int:
        return self.dq.pop()

    def peek(self) -> int:
        return self.dq[-1]
        
    def empty(self) -> bool:
        return not self.dq
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()