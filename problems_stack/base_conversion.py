# Convert decimal number to binary
from stack import stack_01


def divideby2(dec_num):
    reminder_stack = stack_01.Stack()

    while dec_num > 0:
        reminder_stack.push(dec_num % 2)
        dec_num = dec_num // 2

    bin_string = ""
    while not reminder_stack.isEmpty():
        bin_string = bin_string + str(reminder_stack.pop())

    return bin_string


print(divideby2(28))


# More generic function

def dividebybase(decimal_num, base):
    reminder_stack = stack_01.Stack()
    digits = "0123456789ABCDEF"
    while decimal_num > 0:
        reminder_stack.push(decimal_num % base)
        decimal_num = decimal_num // base

    bin_string = ""
    while not reminder_stack.isEmpty():
        bin_string = bin_string + digits[reminder_stack.pop()]

    return bin_string


print(dividebybase(28, 16))
