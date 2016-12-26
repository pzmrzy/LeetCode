class Solution(object):
    def merge(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
            if nums1 > nums2:
                ans.append(nums1[0])
                nums1.pop(0)
            else:
                ans.append(nums2[0])
                nums2.pop(0)
        return ans

    def get(self, num, k):
        n = len(num)
        ret = [0] * k
        j = 0
        for i in range(n):
            while n - i + j > k and j > 0 and ret[j - 1] < num[i]:
                j -= 1
            if j < k:
                ret[j] = num[i]
                j += 1
        return ret;

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = "0" * k
        l1, l2 = len(nums1), len(nums2)
        for i in range(k + 1):
            if i <= l1 and k - i <= l2:
                tmp1, tmp2 = self.get(nums1, i), self.get(nums2, k - i)
                res = self.merge(tmp1, tmp2)
                t = "".join(map(str, res))
                if t > ans:
                    ans = t
        return [int(i) for i in ans]
