class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        stack = range(n - 1, -1, -1)
        for i in range(n - 1, -1, -1):
            res[i] = -1
            while len(stack) > 0 and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if len(stack) > 0:
                res[i] = nums[stack[-1]]
            stack.append(i)
        return res
