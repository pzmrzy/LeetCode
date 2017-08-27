class Solution(object):
    def dfs(self, a, i, sum1, sum2, sum3, sum4, wid):
        if sum1 > wid or sum2 > wid or sum3 > wid or sum4 > wid:
            return False
        if i == -1:
            if sum1 == sum2 == sum3 == sum4:
                return True
            else:
                return False
        return self.dfs(a, i - 1, sum1 + a[i], sum2, sum3, sum4, wid) or self.dfs(a, i - 1, sum1, sum2 + a[i], sum3, sum4, wid) or self.dfs(a, i - 1, sum1, sum2, sum3 + a[i], sum4, wid) or self.dfs(a, i - 1, sum1, sum2, sum3, sum4 + a[i], wid)
        
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        summ, l = sum(nums), len(nums)
        if summ % 4 != 0 or l < 4:
            return False
        sum1 = sum2 = sum3 = sum4 = 0
        nums.sort()
        return self.dfs(nums, l - 1, sum1, sum2, sum3, sum4, summ / 4)
