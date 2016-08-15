import math
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        res = [0,1]
        for i in range(int(math.log(num,2))):
            res += map(lambda x:x+1, res)
            
        return res[:num+1]
