from stack.stack_01 import Stack


class BalancedParenthesis():
    def __init__(self, parenthesis):
        self.items = parenthesis

    def check(self):
        s = Stack()
        i = 0
        balanced = True
        while i < len(self.items) and balanced:
            if i == '(':
                s.push(i)
            else:
                if s.isEmpty():
                    balanced = False
                else:
                    s.pop()
            i += 1
        if s.isEmpty and balanced:
            return True
        else:
            return False


b = BalancedParenthesis("((((())")
print(b.check())
