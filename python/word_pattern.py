class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ob = str.split(' ')
        dic = {}
        result = True
        i = 0
        if (len(ob) != len(pattern)):
            return False
        for ch in pattern:
            if not(dic.has_key(ch)):
                if (ob[i] in dic.values()):
                    return False
                dic[ch] = ob[i]
            else:
                if (dic[ch] != ob[i]):
                    result = False
                    break
            i += 1
        return result
