class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        visit = [False] * n
        res = 0
        now = 0
        for i in range(n):
            if visit[i]:
                continue
            tmp = nums[i]
            while not visit[tmp]:
                now += 1
                visit[tmp] = True
                tmp = nums[tmp]
            res = max(res, now)
            now = 0
        return res
