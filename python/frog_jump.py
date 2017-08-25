class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        def reach(s, last, pos, jump):
            if pos + jump - 1 <= last <= pos + jump + 1:
                return True
            if pos + jump + 1 in s:
                if reach(s, last, pos + jump + 1, jump + 1):
                    return True
            if pos + jump in s:
                if reach(s, last, pos + jump, jump):
                    return True
            if jump > 1 and pos + jump - 1 in s:
                if reach(s, last, pos + jump - 1, jump - 1):
                    return True
            return False
        
        l = len(stones)
        if l == 0:
            return False
        if l == 1:
            return True
        if stones[1] != 1:
            return False
        if l == 2:
            return True
        s = set()
        for i in range(l):
            if i > 3 and stones[i] > 2 * stones[i - 1]:
                return False
            else:
                s.add(stones[i])
        return reach(s, stones[-1], 1, 1)
