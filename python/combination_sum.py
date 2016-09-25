class Solution(object):
    def com(self, ind, summ, path):
        if summ == self.target:
            self.res.append(path)
            return
        for i in range(ind, self.n):
            tmp = summ + self.candidates[i]
            if tmp <= self.target:
                self.com(i, tmp, path+[self.candidates[i]])
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.target = target
        self.candidates = candidates
        self.n = len(candidates)
        self.com(0, 0, [])
        return self.res
