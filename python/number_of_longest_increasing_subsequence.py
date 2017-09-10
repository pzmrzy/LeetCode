class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lis = [0] * n
        way = [0] * n
        for i in range(n - 1, -1, -1):
            lis[i] = 1
            way[i] = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    if 1 + lis[j] > lis[i]:
                        lis[i] = lis[j] + 1
                        way[i] = way[j]
                    elif 1 + lis[j] == lis[i]:
                        way[i] += way[j]
        return sum([w if l == max(lis) else 0 for w, l in zip(way, lis)])
