class MyQueue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    #Transfer elements from stack 1 to stack 2
    def enqueue(self,value):
        while len(self.stack1) > 0 :
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        
        while len(self.stack2)>0:
            self.stack1.append(self.stack2.pop())
        
    def peek(self):
        return self.stack1[-1]
    
    def is_empty(self):
        return len(self.stack1) == 0
    
    
q = MyQueue
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Front of the queue:",q.peek())
print("Is the queue empty?",q.is_empty())

    