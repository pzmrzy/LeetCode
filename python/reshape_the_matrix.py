class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return nums
        if len(nums[0]) == 0:
            return nums
        if r * c == len(nums) * len(nums[0]):
            g = iter(sum(nums, []))
            return [[next(g) for _ in range(c)] for _ in range(r)]
        else:
            return nums
