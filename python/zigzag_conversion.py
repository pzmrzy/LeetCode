ass Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        dic = {}
        for i in range(numRows):
            dic[i] = []
        now = 0
        inc = 1
        for c in s:
            dic[now].append(c)
            now += inc
            if now == numRows:
                now = numRows - 2
                inc = -1
            elif now == 0:
                now == 1
                inc = 1
        res = ""
        for i in range(numRows):
            res += "".join(dic[i])
        
        return res
