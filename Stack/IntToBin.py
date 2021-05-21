"""
Divide by 2 method

242 -> 11110010

242 // 2 = 121, 0
121 // 2 = 60,  1
60 // 2 = 30    0
30 // 2 = 15    0
15 // 2 = 7     1
7 // 2 = 3      1
3 // 2 = 1      1
1 // 2 = 0      1



"""
from Stack import Stack

def intToBin(num):
    stack = Stack()

    while num > 0:
        rem = num % 2
        stack.push(rem)
        num = num // 2

    binaryNum = ""
    while not stack.isEmpty():
        binaryNum += str(stack.pop())

    return binaryNum

print(intToBin(242))
