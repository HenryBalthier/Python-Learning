class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.m = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.s += [x]
        if len(self.s) == 1:
            self.m += [x]
        elif x <= self.m[-1]:
            self.m += [x]

    def pop(self):
        """
        :rtype: void
        """
        if self.s[-1] == self.m[-1]:
            self.m = self.m[:-1]
        self.s = self.s[:-1]

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.m[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    s = MinStack()
    s.push(1)
    s.push(2)
    print(s.s)
    print(s.getMin())
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.s)