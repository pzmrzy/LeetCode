class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        res = 0
        dic = {0: 0}
        for l in input.split('\n'):
            name = l.lstrip('\t')
            dep = len(l) - len(name)
            if '.' in name:
                res = max(res, dic[dep] + len(name))
            else:
                dic[dep + 1] = dic[dep] + len(name) + 1
        return res
