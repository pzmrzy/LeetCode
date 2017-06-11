from collections import defaultdict
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        edge = defaultdict(lambda: [])
        for x, y in zip(ppid, pid):
            edge[x].append(y)
        q = [kill]
        now = 0
        while now < len(q):
            root = q[now]
            for ch in edge[root]:
                q.append(ch)
            now += 1
        return q
        
