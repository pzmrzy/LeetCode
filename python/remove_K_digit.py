class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        t=k
        for i in range(k):
            if t >= len(num):
                return "0"
            for j in range(len(num) - 1):
                if num[j] <= num[j + 1]:
                    if j == len(num) - 2:
                        num = num[:-1].lstrip('0')
                else:
                    num = (num[:j] + num[j + 1:]).lstrip('0')
                    break
            t -= 1
        res = num.lstrip('0')
        if res == "":
            res = "0"
        return res
