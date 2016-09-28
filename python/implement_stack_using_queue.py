class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.front = None

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.front = x
        self.queue1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty():
            return None
        while len(self.queue1) > 1:
            x = self.queue1[0]
            self.queue2.append(x)
            del self.queue1[0]
        x = self.queue1[0]
        del self.queue1[0]
        self.queue1, self.queue2 = self.queue2, self.queue1
        return x

    def top(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        x = None
        while len(self.queue1) > 0:
            x = self.queue1[0]
            self.queue2.append(x)
            del self.queue1[0]
        self.queue1, self.queue2 = self.queue2, self.queue1
        return x

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue1) == 0
