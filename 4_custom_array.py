class IntList:
    def __init__(self):
        self.data = []

    def append(self, x):
        if isinstance(x, int):
            self.data.append(x)
        else:
            raise TypeError("Only integers allowed")

    def remove(self, x):
        self.data.remove(x)

    def pop(self, index=-1):
        return self.data.pop(index)

    def slice(self, start=None, end=None):
        return self.data[start:end]

# Example
lst = IntList()
lst.append(5)
lst.append(10)
print(lst.slice())
