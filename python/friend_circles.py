class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
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
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                else:
                    parent[p1] = p2
                    if rank[p1] == rank[p2]:
                        rank[p2] += 1
        
        l = len(M)
        parent = {i: i for i in range(l)}
        rank = {}
        for i in range(l):
            for j in range(l):
                if M[i][j] == 0:
                    continue
                union(i, j)
        [find(i) for i in range(l)]
        return len(set(parent.values()))    
        
