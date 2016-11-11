class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        if m == 0:
            return
        n = len(rooms[0])
        q = []
        inf = 2147483647
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
                    
        while len(q) > 0:
            i, j, d = q.pop(0)
            if i - 1 >= 0:
                if rooms[i - 1][j] == inf:
                    rooms[i - 1][j] = d + 1
                    q.append((i - 1, j, d + 1))
            if i + 1 < m:
                if rooms[i + 1][j] == inf:
                    rooms[i + 1][j] = d + 1
                    q.append((i + 1, j, d + 1))
            if j - 1 >= 0:
                if rooms[i][j - 1] == inf:
                    rooms[i][j - 1] = d + 1
                    q.append((i, j - 1, d + 1))
            if j + 1 < n:
                if rooms[i][j + 1] == inf:
                    rooms[i][j + 1] = d + 1
                    q.append((i, j + 1, d + 1))
        
