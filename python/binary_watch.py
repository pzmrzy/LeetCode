class Solution(object):
    def count(self, n):
        c = 0
        while c < n:
            n &= (n - 1)
            c += 1
        return c
        
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num > 10:
            return []
        hour = {key:[] for key in range(11)}
        minute = {key:[] for key in range(11)}
        for i in range(12):
            hour[self.count(i)].append(i)
        for i in range(60):
            minute[self.count(i)].append(i)
        res = []
        for i in range(num+1):
            for x in hour[i]:
                for y in minute[num-i]:
                    if len(str(y)) == 1:
                        y = "0" + str(y)
                    res.append("%s:%s" % (x, y))
        return res
