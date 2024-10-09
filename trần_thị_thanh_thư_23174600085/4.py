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
            print("Ngăn xếp rỗng, không thể pop!")
            return None
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng!")
            return None
        return self.stack[-1]

stack = Stack(5)  

stack.push(1.1)
stack.push(2.2)
stack.push(3.3)
stack.push(4.4)
stack.push(5.5)

stack.push(6.6)

print(stack.pop())  
print(stack.pop())  
print(stack.peek())  
print(stack.isEmpty()) 
