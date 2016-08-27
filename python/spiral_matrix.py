class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        for i in range(m):
            matrix[i] = ['#'] + matrix[i] + ['#']
        matrix = [['#'] * (n+2)] + matrix + [['#'] * (n+2)]
        
        nowx = 1
        nowy = 1
        dir = 0
        t = m * n
        while len(res) < t:
            res.append(matrix[nowx][nowy])
            matrix[nowx][nowy] = '#'
            if dir == 0:
                nowy += 1
                if matrix[nowx][nowy] == '#':
                    dir = 1
                    nowy -= 1
                    nowx += 1
            elif dir == 1:
                nowx += 1
                if matrix[nowx][nowy] == '#':
                    dir = 2
                    nowx -= 1
                    nowy -= 1
            elif dir == 2:
                nowy -= 1
                if matrix[nowx][nowy] == '#':
                    dir = 3
                    nowy += 1
                    nowx -= 1
            else:
                nowx -= 1
                if matrix[nowx][nowy] == '#':
                    dir = 0
                    nowx += 1
                    nowy += 1
        return res
