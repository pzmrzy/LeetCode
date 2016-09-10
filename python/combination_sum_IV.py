class Solution(object):
    def f(self, i):
        res = 0
        for k in self.nums:
            if i - k < 0:
                continue
            if self.data[i-k] == -1:
                self.f(i-k)
            res += self.data[i-k]
        self.data[i] = res
        return res
        
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums = []
        for i in nums:
            if i <= target:
                self.nums.append(i)
        if len(self.nums) == 0:
            return 0
        self.minn = min(nums)
        self.data = [-1 for i in range(target+1)]
        self.data[self.minn] = 1
        for i in range(self.minn):
            self.data[i] = 0
        self.data[0] = 1
        return self.f(target)
