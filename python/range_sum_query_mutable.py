class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.l = len(nums)
        self.c = [0] * (self.l + 1)
        self.nums = [0] * (self.l + 1)
        for i in range(self.l):
            self.update(i, nums[i])
            self.nums[i] = nums[i]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        delta = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= self.l:
            self.c[i] += delta
            i += i & -i

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        j += 1
        res = 0
        while j > 0:
            res += self.c[j]
            j -= j & -j
        while i > 0:
            res -= self.c[i]
            i -= i & -i
        return res


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
