class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in '+-*':
                tmp1 = self.diffWaysToCompute(input[:i])
                tmp2 = self.diffWaysToCompute(input[i + 1:])
                for j in tmp1:
                    for k in tmp2:
                        res.append(self.cal(j, k, input[i]))
        return res
    def cal(self, x, y, op):
        if op == '+':
            return x + y
        if op == '-':
            return x - y
        return x * y
