class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pq = [(x[0], i, 0) for i, x in enumerate(nums)]
        heapq.heapify(pq)
        ans = [float('-inf'), float('inf')]
        right = max([x[0] for x in nums])
        while True:
            left, i, j = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = [left, right]
            if j + 1 == len(nums[i]):
                return ans
            v = nums[i][j + 1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j + 1))
