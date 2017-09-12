from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        q1 = deque()
        q2 = deque()
        for i, c in enumerate(senate):
            if c == 'R':
                q1.append(i)
            else:
                q2.append(i)
        n = len(senate)
        while len(q1) > 0 and len(q2) > 0:
            r, d = q1.popleft(), q2.popleft()
            if r < d:
                q1.append(r + n)
            else:
                q2.append(d + n)
        return "Radiant" if len(q1) > len(q2) else "Dire"
