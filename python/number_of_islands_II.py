class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]
            
        def union(v1, v2):
            p1 = find(v1)
            p2 = find(v2)
            if p1 not in rank:
                rank[p1] = 0
            if p2 not in rank:
                rank[p2] = 0
            if p1 != p2:
                self.res -= 1
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                else:
                    parent[p1] = p2
                    if rank[p1] == rank[p2]:
                        rank[p2] += 1
                        
        parent = {}
        rank = {}
        grid = set()
        self.res = 0
        ret = []
        for x, y in positions:
            self.res += 1
            grid.add((x, y))
            parent[(x, y)] = (x, y)
            if (x - 1, y) in grid:
                union((x, y), (x - 1, y))
            if (x + 1, y) in grid:
                union((x, y), (x + 1, y))
            if (x, y - 1) in grid:
                union((x, y), (x, y - 1))
            if (x, y + 1) in grid:
                union((x, y), (x, y + 1))
            ret.append(self.res)
        return ret
