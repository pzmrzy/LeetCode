import Queue
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small, self.large = Queue.PriorityQueue(), Queue.PriorityQueue()
        self.even = True
        
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if self.even:
            self.small.put(-num)
            tmp = self.small.get()
            self.large.put(-tmp)
        else:
            self.large.put(num)
            tmp = self.large.get()
            self.small.put(-tmp)
        self.even = not self.even

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        ts = tl = 0
        if self.large.qsize() > 0:
            tl = self.large.get()
            self.large.put(tl)
        if self.small.qsize() > 0:
            ts = self.small.get()
            self.small.put(ts)
            
        return (tl - ts) / 2.0 if self.even else tl
            

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
