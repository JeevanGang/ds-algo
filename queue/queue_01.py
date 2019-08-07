import stack_01


class Queue():
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()


q = Queue()
q.enqueue(2)
q.enqueue(3)
print(q.size())
