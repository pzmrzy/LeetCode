class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        
    def empty(self):
        return len(self.data) == 0
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.empty():
            self.data.append((x, x))
        else:
            self.data.append((x, min(x, self.data[-1][1])))

    def pop(self):
        """
        :rtype: void
        """
        del self.data[-1]

    def top(self):
        """
        :rtype: int
        """
        t = self.data[-1][0]
        #del self.data[-1]
        return t

    def getMin(self):
        """
        :rtype: int
        """
        if self.empty():
            return
        else:
            return self.data[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
