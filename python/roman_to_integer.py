ass Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) == 0):
            return 0
        dic = {}
        dic['M'] = 1000;
        dic['D'] = 500;
        dic['C'] = 100;
        dic['L'] = 50;
        dic['X'] = 10;
        dic['V'] = 5;
        dic['I'] = 1;
        res = 0
        for i in range(len(s) - 1):
            if (dic[s[i]] < dic[s[i + 1]]):
                res -= dic[s[i]]
            else:
                res += dic[s[i]]
        res += dic[s[-1]]
        return res
            
            
