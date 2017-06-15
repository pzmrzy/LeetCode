class Solution(object):
    def find(self, num, great):
        if great == -1:
            return great
        if great > num:
            return great
        return self.find(num, self.dic[great])
        
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(findNums) == 0:
            return []
        self.dic = {}
        self.dic[nums[-1]] = -1
        for i in range(len(nums) - 2, -1, -1):
            self.dic[nums[i]] = self.find(nums[i], nums[i + 1])
        res = []
        for n in findNums:
            res.append(self.dic[n])
        return res
