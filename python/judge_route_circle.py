class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        nowx, nowy = 0, 0
        for x in moves:
            if x == 'L':
                nowx -= 1
            if x == 'R':
                nowx += 1
            if x == 'U':
                nowy += 1
            if x == 'D':
                nowy -= 1
        return nowx == 0 and nowy == 0
