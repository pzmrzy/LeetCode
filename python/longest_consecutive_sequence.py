from collections import defaultdict
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
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
                        
        parent = {}
        rank = {}
        close = set()
        for n in nums:
            close.add(n)
            parent[n] = n
            if n - 1 in close:
                union(n, n-1)
            if n + 1 in close:
                union(n, n + 1)
        res = defaultdict(lambda: 0)
        for n in nums:
            find(n)
        for i in parent.values():
            res[i] += 1
        return max(res.values())
