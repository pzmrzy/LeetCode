class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.front = None    
    
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self.stack1) == 0:
            self.front = x
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.stack2) == 0:
            while (len(self.stack1) > 0):
                self.stack2.append(self.stack1.pop())
        self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack2) > 0:
            return self.stack2[-1]
        else:
            return self.front
            
    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0
