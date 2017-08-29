class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, v in enumerate(nums):
            if target - v in dic:
                return [dic[target - v], i]
            dic[v] = i

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind = {}
        n = len(nums)
        for i in range(n):
            ind.setdefault(nums[i], [])
            ind[nums[i]].append(i)
        nums.sort()
        
        for i in range(n - 1):
            t = target - nums[i]
            l = i + 1
            r = n - 1
            while l <= r:
                mid = (l + r) / 2
                if nums[mid] == t:
                    if nums[i] == nums[mid]:
                        return [ind[nums[i]][0], ind[nums[i]][1]]
                    return [ind[nums[i]][0], ind[nums[mid]][0]]
                elif nums[mid] < t:
                    l = mid + 1
                else:
                    r = mid - 1
