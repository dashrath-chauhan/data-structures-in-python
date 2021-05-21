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

def is_match(p1, p2):
    if(p1 == "{" and p2 == "}") or (p1 == "}" and p2 == "{"):
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "(" and p2 == ")":
        return True
    else:
        return False
    
def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        
        if paren in "{[(":
            s.push(paren)
        else:
            if s.isEmpty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top,paren):
                    is_balanced = False
        index += 1

    if s.isEmpty() and is_balanced:
        return True
    else:
        return False

print(is_paren_balanced("{}{)"))















    
