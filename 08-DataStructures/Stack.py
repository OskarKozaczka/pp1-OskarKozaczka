class Stack:

    def __init__(self):
        self.stack = []
    def __str__(self):
        return str(self.stack)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack)==0
    
    
    
Stos=Stack()

Stos.push(1)
print(Stos)
Stos.push(2)
print(Stos)
Stos.push(3)
print(Stos)
Stos.push(4)
print(Stos)
Stos.push(5)
print(Stos)
print(Stos.pop())
print(Stos.pop())
print(Stos.pop())