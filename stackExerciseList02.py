#Given a string/word , remove all pairs(2 consecutive same character) 
#characters which occur consecutively and continue till no such pair 
#exist


class Stack:
    
    def __init__(self):
        self.stack_list = []
    
    def print_stack(self):
        for i in range(len(self.stack_list)-1,-1,-1):
            print(self.stack_list[i])
    
    def is_empty(self):
        return len(self.stack_list) == 0
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]
            
    def size(self):
        return len(self.stack_list)
    
    def push(self,value):
        self.stack_list.append(value)
        
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
            
            
def remove_pairs(input_str):
    
    myStack = Stack()
    
    for char in input_str:
        if not myStack.is_empty() and char == myStack.peek():
            myStack.pop()
        else:
            myStack.push(char)
    return "".join(myStack.stack_list)
    
        
        
print(remove_pairs("abbaca")) # Debería devolver "ca"