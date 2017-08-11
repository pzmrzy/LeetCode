from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c = Counter(tasks)
        maxx = max(c.values())
        return max(len(tasks), (maxx - 1) * (n + 1) + len(c.values()) - len(filter(lambda x: x != maxx, c.values())))
