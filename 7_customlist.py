class AdvancedList:
    def __init__(self):
        self.data = []
        self.history = []
        self.redo_stack = []

    def append(self, val):
        self.data.append(val)
        self.history.append(('append', val))

    def insert(self, index, val):
        self.data.insert(index, val)
        self.history.append(('insert', index, val))

    def remove(self, val):
        self.data.remove(val)
        self.history.append(('remove', val))

    def pop(self, index=-1):
        val = self.data.pop(index)
        self.history.append(('pop', index, val))
        return val

    def reverse(self):
        self.data.reverse()
        self.history.append(('reverse',))

    def sort(self):
        self.data.sort()
        self.history.append(('sort',))

    def undo(self):
        if not self.history:
            return
        action = self.history.pop()
        self.redo_stack.append(action)
        cmd = action[0]

        if cmd == 'append':
            self.data.pop()
        elif cmd == 'insert':
            self.data.pop(action[1])
        elif cmd == 'remove':
            self.data.append(action[1])
        elif cmd == 'pop':
            self.data.insert(action[1], action[2])
        elif cmd == 'reverse':
            self.data.reverse()
        elif cmd == 'sort':
            self.data.sort(reverse=True)

# Example
alist = AdvancedList()
alist.append(5)
alist.append(2)
alist.sort()
alist.undo()
print(alist.data)
