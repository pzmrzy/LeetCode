class Solution(object):
    dic = {}
    def find(self, p):
        if p != self.dic[p]:
            t = self.find(self.dic[p])
            self.dic[p] = t
            return t
        else:
            return p
    def join(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        if i > j:
            self.dic[q] = i
        else:
            self.dic[p] = j
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        for n in nums:
            self.dic[n] = n
        for n in nums:
            if self.dic.has_key(n + 1):
                self.join(n, n + 1)
            if self.dic.has_key(n - 1):
                self.join(n, n - 1)
            
        for n in nums:
            self.find(n)
        res = {}
        for key in self.dic:
            res.setdefault(self.dic[key], 0)
            res[self.dic[key]] += 1
        return max(res.values())
