class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        target = collections.defaultdict(lambda: 0)
        for c in s1:
            target[c] += 1
        now = collections.defaultdict(lambda: 0)
        for i, x in enumerate(s2):
            now[x] += 1
            if i >= len(s1):
                t = s2[i - len(s1)]
                now[t] -= 1
                if now[t] == 0:
                    now.pop(t)
            if now == target:
                return True
        return False
