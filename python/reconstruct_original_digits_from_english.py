class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for i in range(26):
            dic[chr(97 + i)] = 0
        res = [0 for i in range(10)]
        for i in s:
            dic[i] += 1
            
        #4 u
        res[4] = dic['u']
        for x in "four":
            dic[x] -= res[4]
            
        #0 z
        res[0] = dic['z']
        for x in "zero":
            dic[x] -= res[0]
        
        #8 g
        res[8] = dic['g']
        for x in "eight":
            dic[x] -= res[8]
            
        #6 x
        res[6] = dic['x']
        for x in "six":
            dic[x] -= res[6]
            
        #7 s
        res[7] = dic['s']
        for x in "seven":
            dic[x] -= res[7]
            
        #2 w
        res[2] = dic['w']
        for x in "two":
            dic[x] -= res[2]
            
        #1 o
        res[1] = dic['o']
        for x in "one":
            dic[x] -= res[1]
        
        #9 2n
        res[9] = dic['n'] / 2
        for x in "nine":
            dic[x] -= res[9]
        
        #3 t
        res[3] = dic['t']
        for x in "three":
            dic[x] -= res[3]
        
        #5 v
        res[5] = dic['v']
        for x in "five":
            dic[x] -= res[5]
            
        ret = ""
        for i in range(10):
            ret += str(i) * res[i]
        return ret
        
