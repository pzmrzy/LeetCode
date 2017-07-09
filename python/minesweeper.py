class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        click = tuple(click)
        R, C = len(board), len(board[0])
        
        def neighbour(r, c):
            ret = []
            for x in xrange(-1, 2):
                for y in xrange(-1, 2):
                    if (x or y) and 0 <= r + x < R and 0 <= c + y < C:
                        ret.append((r + x, c + y))
            return ret
        
        stack = [click]
        visit = {click}
        while stack:
            r, c = stack.pop()
            if board[r][c] == 'M':
                board[r][c] = 'X'
            else:
                num = sum(board[nr][nc] in 'MX' for nr, nc in neighbour(r, c))
                if num:
                    board[r][c] = str(num)
                else:
                    board[r][c] = 'B'
                    for nei in neighbour(r, c):
                        if board[nei[0]][nei[1]] in 'ME' and nei not in visit:
                            stack.append(nei)
                            visit.add(nei)
        return board
