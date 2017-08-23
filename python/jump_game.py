class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for i, n in enumerate(nums):
            if i > reach:
                return False
            reach = max(i + n, reach)
        return True

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p1, p2 = len(nums)-1, len(nums)-1
        while p1 >= 0:
            if p1 + nums[p1] >= p2:
                p2 = p1
            p1 -= 1
        return p2 == 0
