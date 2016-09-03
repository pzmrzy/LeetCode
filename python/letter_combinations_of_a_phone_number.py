class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':"abc", '3':"def", '4':"ghi", '5':"kjl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        tmp = [""]
        res = []
        for c in digits:
            res = [x+y for x in tmp for y in dic[c]]
            tmp = res
        return res
