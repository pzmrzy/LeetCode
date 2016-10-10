class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        res = ""
        c = 0
        if l1 < l2:
            num1 = num1.zfill(l2)
            l = l2
        else:
            num2 = num2.zfill(l1)
            l = l1
        for i in range(l-1, -1, -1):
            t = int(num1[i]) + int(num2[i]) + c
            res = str(t % 10) + res
            c = t / 10
        if c == 1:
            res = "1" + res
        return res
