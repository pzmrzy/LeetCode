from collections import defaultdict
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = defaultdict(lambda :0)
        for c in s:
            dic[c] += 1
        res = ""
        for key, val in sorted(dic.items(), key = lambda x: -x[1]):
            res += val * key
        return res
