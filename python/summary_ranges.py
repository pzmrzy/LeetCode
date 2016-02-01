class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        begin = 0
        end = 1
        nums.append('-1')
        now = nums[0]
        l = len(nums)
        for i in range(l-1):
            if (nums[end] != now + 1):
                if (begin + 1 == end):
                    tmp = str(now)
                else:
                    tmp = "%d->%d" % (nums[begin], now)
                print tmp
                begin = end
                end += 1
                now = nums[begin]
                result.append(tmp)
            else:
                end += 1
                now += 1
        return result

