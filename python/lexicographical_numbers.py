class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        now = 1
        for i in range(n):
            res.append(now)
            if now * 10 <= n:
                now *= 10
            elif now % 10 != 9 and now + 1 <= n:
                now += 1
            else:
                while now / 10 % 10 == 9:
                    now /= 10
                now = now / 10 + 1
        return res
