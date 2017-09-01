class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return
        stack = []
        board[:] = [[c for c in row] for row in board]
        for i in range(m):
            if board[i][0] == 'O':
                stack.append((i, 0))
            if board[i][n - 1] == 'O':
                stack.append((i, n - 1))
        for i in range(n):
            if board[0][i] == 'O':
                stack.append((0, i))
            if board[m - 1][i] == 'O':
                stack.append((m - 1, i))
        while stack:
            i, j = stack.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = "S"
                stack.extend([(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)])
        board[:] = [''.join(['XO'[c == 'S'] for c in row]) for row in board]
