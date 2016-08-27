class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        res = [[-1] * (n + 2)]
        for i in range(n):
            res.append([-1] + [0] * n + [-1])
        res.append([-1] * (n + 2))
        nowx = 1
        nowy = 1
        dir = 0
        t = n * n
        for i in range(t):
            res[nowx][nowy] = i + 1
            if dir == 0:
                nowy += 1
                if res[nowx][nowy] != 0:
                    dir = 1
                    nowy -= 1
                    nowx += 1
            elif dir == 1:
                nowx += 1
                if res[nowx][nowy] != 0:
                    dir = 2
                    nowx -= 1
                    nowy -= 1
            elif dir == 2:
                nowy -= 1
                if res[nowx][nowy] != 0:
                    dir = 3
                    nowy += 1
                    nowx -= 1
            else:
                nowx -= 1
                if res[nowx][nowy] != 0:
                    dir = 0
                    nowx += 1
                    nowy += 1
                    
        return [t[1:n + 1] for t in res[1:n + 1]]
