class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        pretime = 0
        for log in logs:
            fun, types, ts = log.split(':')
            fun, ts = int(fun), int(ts)
            if types == "start":
                if stack:
                    res[stack[-1]] += ts - pretime
                stack.append(fun)
                pretime = ts
            else:
                res[stack.pop()] += ts - pretime + 1
                pretime = ts + 1
        return res
