from collections import deque
class Stackusingqueue:
    def __init__(self,item):
        self.queue=deque()
    def push(self,item):
        self.queue.qppend(item)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
    def pop(self):
        if(len(self.queue)==0):
            return "stack is empty"
        return self.queue.popleft()
    def peek(self):
         if(len(self.queue)==0):
            return "stack is empty"
         return self.queue[0]
    def
