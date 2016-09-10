class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return len(nums)
        now = nums[0]
        flag = 0
        res = 1
        for i in range(n - 1):
            if nums[i+1] == now:
                continue
            if nums[i+1] > now:
                if flag != -1:
                    flag = -1
                    res += 1
            if nums[i+1] < now:
                if flag != 1:
                    flag = 1
                    res += 1
            now = nums[i+1]
        return res
