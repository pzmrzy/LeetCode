class Solution(object):
    def check(self, x, y, X, Y):
        if ((x < 0) or (y < 0) or (x > X) or (y > Y)):
            return False
        else:
            return True
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        X = len(board) - 1
        Y = len(board[0]) - 1
        for i in range(X + 1):
            for j in range(Y + 1):
                live = board[i][j] / 10
                status = board[i][j] % 10
                if (self.check(i, j + 1, X, Y)):
                    if (board[i][j + 1] % 10 == 1):
                        live += 1
                    if (status == 1):
                        board[i][j + 1] += 10;
                if (self.check(i + 1, j - 1, X, Y)):
                    if (board[i + 1][j - 1] % 10 == 1):
                        live += 1
                    if (status == 1):
                        board[i + 1][j - 1] += 10
                if (self.check(i + 1, j, X, Y)):
                    if (board[i + 1][j] % 10 == 1):
                        live += 1
                    if (status == 1):
                        board[i + 1][j] += 10
                if (self.check(i + 1, j + 1, X, Y)):
                    if (board[i + 1][j + 1] % 10 == 1):
                        live += 1
                    if (status == 1):
                        board[i + 1][j + 1] += 10
                if (status == 0):
                    if (live == 3):
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                if (status == 1 and live < 2):
                    board[i][j] = 0
                if (status == 1 and live > 3):
                    board[i][j] = 0
                if (status == 1 and (live == 2 or live == 3)):
                    board[i][j] = 1
