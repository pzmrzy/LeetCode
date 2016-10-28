class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.xcol = [0 for i in range(n)]
        self.xrow = [0 for i in range(n)]
        self.xd1 = 0
        self.xd2 = 0
        self.ycol = [0 for i in range(n)]
        self.yrow = [0 for i in range(n)]
        self.yd1 = 0
        self.yd2 = 0
        self.n = n
        
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
            n = self.n
            self.xcol[col] += 1
            if self.xcol[col] == n:
                return 1
            self.xrow[row] += 1
            if self.xrow[row] == n:
                return 1
                
            if col == row:
                self.xd1 += 1
            if n - row - 1 == col:
                self.xd2 += 1
            
            if self.xd1 == n:
                return 1
            if self.xd2 == n:
                return 1
                
        if player == 2:
            n = self.n
            self.ycol[col] += 1
            if self.ycol[col] == n:
                return 2
            self.yrow[row] += 1
            if self.yrow[row] == n:
                return 2
            if col == row:
                self.yd1 += 1
            if n - row - 1 == col:
                self.yd2 += 1
            if self.yd1 == n:
                return 2
            if self.yd2 == n:
                return 2
        return 0
                    
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
