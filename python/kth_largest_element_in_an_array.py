class Solution(object):
    def find(self, nums, k):
        l = len(nums)
        if k == 1:
            return min(nums)
        mid = nums[0]
        left = []
        right = []
        emid = 1
        for n in nums[1:]:
            if n < mid:
                left.append(n)
            elif n > mid:
                right.append(n)
            else:
                emid += 1
        # if len(left) < k <= len(left) + emid:
        #     return mid
        if len(left) < k <= len(left) + emid:
            return mid
        if len(left) == k:
            return max(left)
        if len(left) > k:
            return self.find(left, k)
        if len(left) < k:
            return self.find(right, k - len(left) - emid)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.find(nums, len(nums) - k + 1)

