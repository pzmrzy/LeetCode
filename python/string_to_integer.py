class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0:
            return 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        flag = 1
        if str[0] == '-':
            flag = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        res = 0
        for c in str:
            if c not in ['1','2','3','4','5','6','7','8','9','0']:
                break
            res *= 10
            res += ord(c)-ord('0')
            if flag == 1:
                if res > 2147483647:
                    return INT_MAX
            else:
                if res > 2147483648:
                    return INT_MIN
        return res * flag
