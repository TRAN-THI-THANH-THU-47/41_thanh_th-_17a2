class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.capacity

    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy!")
        else:
            self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng!")
            return None
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng!")
            return None
        return self.stack[-1]

    def count(self):
        return len(self.stack)

    def print_stack(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng!")
        else:
            print("Nội dung ngăn xếp (từ trên xuống dưới):", *reversed(self.stack), sep='\n')

stack = Stack(5)

for value in [1.1, 2.2, 3.3]:
    stack.push(value)

stack.print_stack()

stack.pop()

stack.print_stack()
