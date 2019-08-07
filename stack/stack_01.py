
class Stack():
    '''Implementation of stack Data Structure'''

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


# s = Stack()
# s.push(1)
# s.push(2)
# print(s.pop())
# print(s.peek())
# print(s.size())
