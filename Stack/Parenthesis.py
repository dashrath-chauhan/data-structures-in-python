"""
[] () {} {{()[]}} - balanced
]] ()) {[]((} {{([]}} - not balanced

check for matching closing parenthesis for every opening parenthesis -> using stack compring top element
step1: if opening parenthesis --> push to stack
step2: if closing parenthesis --> pop from stack
step: compare the popped element with the current element which we are looking at

"""
from Stack import Stack

def isMatch(paren1,paren2):
    if paren1 == "{" and paren2 == "}":
        return True
    elif paren1 == "[" and paren2 == "]":
        return True
    elif paren1 == "(" and paren2 == ")":
        return True
    else:
        return False

def isParenBalanced(parenString):
    s = Stack()
    isBalanced = True
    index = 0

    while index < len(parenString) and isBalanced:
        paren = parenString[index]

        if paren in "({[":
            s.push(paren)
        else:
            if s.isEmpty():
                isBalanced = False
            else:
                top = s.pop()
                if not isMatch(top,paren):
                    isBalanced = False
        index += 1

    if s.isEmpty() and isBalanced:
        return True
    else:
        return False

print(isParenBalanced("(){(){()}}[]"))
