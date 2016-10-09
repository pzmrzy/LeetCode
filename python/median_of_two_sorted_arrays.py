class Solution(object):
    def med(self, nums):
        l = len(nums)
        return (nums[l / 2] + nums[l / 2 - 1]) / 2.0 if l % 2 == 0 else nums[l / 2]

    def find(self, A, B, k):
        if k == 1:
            return min(A + B)
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        t = k / 2
        a = A[t - 1] if len(A) >= t else None
        b = B[t - 1] if len(B) >= t else None

        if b is None or (a is not None and a < b):
            return self.find(A[t:], B, k - t)
        else:
            return self.find(A, B[t:], k - t)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 + l2 == 0:
            return 0
        if l1 == 0:
            return self.med(nums2)
        if l2 == 0:
            return self.med(nums1)
        k = (l1 + l2) / 2
        if (l1 + l2) % 2 == 0:
            l = self.find(nums1, nums2, k)
            r = self.find(nums1, nums2, k + 1)
            res = (l + r) / 2.0
        else:
            res = self.find(nums1, nums2, k+1)
        return res
