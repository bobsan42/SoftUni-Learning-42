class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        if not isinstance(element,str): # NOT REQUIRED BY THE PROBLEM
            raise TypeError('Only data of type STRING is supported!')
        else:
            self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        # return '[' + ', '.join(self.data.__reversed__()) + ']'
        return '[' + ', '.join(reversed(self.data)) + ']'

ss = Stack()
ss.push('1')
ss.push('2')

ss.pop()
ss.push('3')
ss.push('aaaa')
print(ss)
