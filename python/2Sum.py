class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n - 2):
            now = nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                #print now, nums[l], nums[r]
                t = now + nums[l] + nums[r] 
                tup = (now, nums[l], nums[r])
                if t == 0:
                    res.append(tup)
                    l += 1
                    r -= 1
                elif t > 0:
                    r -= 1
                else:
                    l += 1
        return list(set(res))
