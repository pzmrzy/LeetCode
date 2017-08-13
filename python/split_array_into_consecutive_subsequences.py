class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for n in nums:
            if n - 1 not in dic:
                if n not in dic:
                    dic[n] = [1]
                else:
                    heapq.heappush(dic[n], 1)
            else:
                l = heapq.heappop(dic[n - 1]) + 1
                if len(dic[n - 1]) == 0:
                    del dic[n - 1]
                if n not in dic:
                    dic[n] = []
                heapq.heappush(dic[n], l)
        for key, arr in dic.items():
            if len(arr) > 0 and min(arr) < 3:
                return False
        return True
