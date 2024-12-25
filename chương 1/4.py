class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
    
    def push(self, value):
        if len(self.stack) < self.size:
            self.stack.append(value)
        else:
            print("Ngăn xếp đã đầy!")
    
    def pop(self):
        if self.is_empty():
            print("Ngăn xếp trống!")
        else:
            return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.size
    
    def count(self):
        return len(self.stack)
    
    def print_stack(self):
        print("Nội dung ngăn xếp:", self.stack)

# Chương trình chính
stack = Stack(5)
stack.push(1.2)
stack.push(3.4)
stack.push(5.6)
stack.print_stack()
stack.pop()
stack.print_stack()
