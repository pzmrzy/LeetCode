import Queue
class Solution(object):
    def check(self, grid, row):
        n = len(grid)
        for i in range(n):
            if grid[i] == row:
                return False
            if (n - i) == abs(grid[i] - row):
                return False
        return True
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        N = n
        q = Queue.LifoQueue()
        q.put([])
        res = []
        while not q.empty():
            now = q.get()
            if len(now) == N:
                res.append(now)
                continue
            for i in range(N):
                if self.check(now, i):
                    q.put(now+[i])
        ans = []
        for n in res:
            tmp = []
            for t in n:
                x = '.'*t+'Q'+'.'*(N-1-t)
                tmp.append(x)
            ans.append(tmp)
        return ans
