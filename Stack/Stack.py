



class Stack():
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def getStack(self):
        return self.stack

    def isEmpty(self):
        return self.stack == []

"""
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.getStack())
stack.push(23)
print(stack.getStack())
print(stack.isEmpty())
stack.pop()
print(stack.getStack())
print(stack.isEmpty())
stack.pop()
stack.pop()
print(stack.getStack())
print(stack.isEmpty())
"""
