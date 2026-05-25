class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        self._move_data()
        return self.output_stack.pop()

    def peek(self) -> int:
        self._move_data()
        return self.output_stack[-1]
        
    def empty(self) -> bool:
        return len(self.input_stack) == 0 and len(self.output_stack) == 0

    def _move_data(self):
        if not self.output_stack:
            while self.input_stack:
                elemt = self.input_stack.pop()
                self.output_stack.append(elemt)
    
# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()

obj.push(1)
obj.push(2)

param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
