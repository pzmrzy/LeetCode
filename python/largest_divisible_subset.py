class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        nums = sorted(nums)
        data = [-1 for _ in range(n)]
        path = [-1 for _ in range(n)]
        data[0] = 1
        for i in range(1, n):
            t = 1
            p = -1
            for j in range(i): 
                if nums[i] % nums[j] == 0:
                    if data[j] + 1 > t:
                        t = data[j] + 1
                        p = j
            data[i] = t
            path[i] = p
        now = data.index(max(data))
        res = []
        while True:
            res = [nums[now]] + res
            now = path[now]
            if now == -1:
                break
        return res
