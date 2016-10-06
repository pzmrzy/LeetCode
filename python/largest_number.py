class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        res = ''.join(sorted(map(str,nums), cmp=lambda x,y: 1 if (x+y)<(y+x) else -1)).lstrip('0')
        return "0" if res == "" else res
