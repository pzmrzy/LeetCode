class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.data = []
        self.size = size
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.data.append(val)
        t = self.data[:-1 - self.size:-1]
        return float(sum(t)) / len(t)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
