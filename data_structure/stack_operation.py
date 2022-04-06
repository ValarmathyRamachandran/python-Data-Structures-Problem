class Stack(object):

    def __init__(self):
        self.lst = []

    def is_empty(self):
        return self.lst == []

    def get_size(self):
        return len(self.lst)

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        if self.is_empty():
            return 'stack underflow'
        return self.lst.pop()

    def display(self):
        print(*self.lst)


stack = Stack()


stack.push(1)
stack.push(2)
stack.push(3)
print(stack.lst)
stack.pop()
print(stack.lst)

