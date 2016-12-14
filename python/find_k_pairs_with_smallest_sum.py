import Queue
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        q = Queue.PriorityQueue()
        l1, l2 = len(nums1), len(nums2)
        if l1 * l2 != 0:
            q.put((nums1[0] + nums2[0], 0, 0))
        res = []
        while len(res) < k and not q.empty():
            s, i, j = q.get()
            res.append([nums1[i], nums2[j]])
            if i < l1 and j + 1 < l2:
                q.put((nums1[i] + nums2[j + 1], i, j + 1))
            if j == 0 and i + 1 < l1:
                q.put((nums1[i + 1] + nums2[0], i + 1, 0))
        return res
