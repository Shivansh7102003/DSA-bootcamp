class Stack():
    def __init__(self):
        self.stack = []
    def is_empty(self):
        if len(self.stack) == 0:
            print("stack is empty")
        
    def push(self , item):
        self.stack.append(item)
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            self.stack.pop()
    def peek(self):
        if self.is_empty():
            print("stack is empty")
        else:
            return self.stack[-1]
    def display(self):
        print("current stack is:" , self.stack)



stack = Stack()
stack.is_empty()
stack.push(5)
stack.push(6)
stack.push(7)
stack.display()
stack.pop()
stack.display()