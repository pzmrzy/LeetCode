class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        res = [0 for i in range(l1 + l2)]
        for i in range(l1):
            for j in range(l2):
                tmp = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                sum = tmp + res[p2]
                res[p1] += sum / 10
                res[p2] = sum % 10
        for i in range(l1 + l2 - 1, 0, -1):
            res[i - 1] += res[i] / 10
            res[i] %= 10
        ans = ''.join(map(str, res)).lstrip('0')
        return '0' if ans == "" else ans
