class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.count = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        queue = self.queue
        queue.append(timestamp)
        self.count += 1
        while len(queue) > 0:
            now = queue[0]
            if now < timestamp - 300:
                del queue[0]
                self.count -= 1
            else:
                break


    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        queue = self.queue
        while len(queue) > 0:
            now = queue[0]
            if now <= timestamp - 300:
                del queue[0]
                self.count -= 1
            else:
                break
        return self.count
