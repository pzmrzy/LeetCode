class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        pos = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    pos.append((i, j))
        self.solve(board, pos)
        
    def solve(self, board, pos):
        for i, j in pos:
            if board[i][j] == '.':
                for c in range(1, 10):
                    if self.check(board, i, j, str(c)):
                        board[i][j] = str(c)
                        if self.solve(board, pos):
                            return True
                        else:
                            board[i][j] = '.'
                return False
        return True
        
    def check(self, board, row, col, c):
        for i in range(9):
            if c in (board[i][col], board[row][i], board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3]):
                return False
        return True
                            
