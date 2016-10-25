class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.tot = len(v1) + len(v2)
        self.data = []
        self.now = 0
        l1 = len(v1)
        l2 = len(v2)
        for i in range(max(l1, l2)):
            if i < l1:
                self.data.append(v1[i])
            if i < l2:
                self.data.append(v2[i])
            
    def next(self):
        """
        :rtype: int
        """
        t = self.data[self.now]
        self.now += 1
        return t
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.now < self.tot

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
