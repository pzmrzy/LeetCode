import Queue
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        dic = {}
        for i in range(m):
            for j in range(n):
                dic.setdefault((i, j), [])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if i + 1 < m and grid[i + 1][j] == '1':
                        dic[(i, j)].append((i + 1, j))
                        dic[(i + 1, j)].append((i, j))
                    if j + 1 < n and grid[i][j + 1] == '1':
                        dic[(i, j)].append((i, j + 1))
                        dic[(i, j + 1)].append((i, j))
        visit = {}
        label = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                if (i, j) in visit:
                    continue
                q = Queue.Queue()
                q.put((i, j))
                visit[(i, j)] = label
                while not q.empty():
                    now = q.get()
                    visit[now] = label
                    for v in dic[now]:
                        if v not in visit:
                            q.put(v)
                            visit[v] = label
                label += 1
        
        return 0 if len(visit) == 0 else max(visit.values())
