class Solution(object):
    def dfs(self, num, tmp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(tmp)
                return
        for i in range(1, len(num) + 1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"):
                self.dfs(num[i:], tmp + "+" + val, cur + int(val), int(val), res)
                self.dfs(num[i:], tmp + "-" + val, cur - int(val), -int(val), res)
                self.dfs(num[i:], tmp + "*" + val, cur - last + last * int(val), last * int(val), res)
    
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res, self.target = [], target
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != "0"):
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)
        return res
