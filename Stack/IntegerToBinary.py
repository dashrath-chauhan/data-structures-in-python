from Stack import Stack


def int_to_bin(num):
    s = Stack()
    while num > 0:
        rem = num % 2
        s.push(rem)
        num = num // 2

    bin_num = ""
    while not s.isEmpty():
        bin_num += str(s.pop())

    return bin_num

def int_to_oct(num):
    s = Stack()
    while num > 0:
        rem = num % 8
        s.push(rem)
        num = num // 8

    oct_num = ""
    while not s.isEmpty():
        oct_num += str(s.pop())

    return oct_num        

print(int_to_bin(242))
print(int_to_oct(242))
