class Solution(object):
    def dfs(self, i, j, tstr):
        if len(tstr) == 0:
            return True
        if i - 1 >= 0 and self.flag[i-1][j] and self.board[i-1][j] == tstr[0]:
            self.flag[i-1][j] = False
            if self.dfs(i - 1, j, tstr[1:]):
                self.flag[i-1][j] = True
                return True
            self.flag[i-1][j] = True
        if i + 1 < self.m and self.flag[i+1][j] and self.board[i+1][j] == tstr[0]:
            self.flag[i+1][j] = False
            if self.dfs(i + 1, j, tstr[1:]):
                self.flag[i+1][j] = True
                return True
            self.flag[i+1][j] = True
        if j - 1 >= 0 and self.flag[i][j-1] and self.board[i][j-1] == tstr[0]:
            self.flag[i][j-1] = False
            if self.dfs(i, j - 1, tstr[1:]):
                self.flag[i][j-1] = True
                return True
            self.flag[i][j-1] = True
        if j + 1 < self.n and self.flag[i][j+1] and self.board[i][j+1] == tstr[0]:
            self.flag[i][j+1] = False
            if self.dfs(i, j + 1, tstr[1:]):
                self.flag[i][j+1] = True
                return True
            self.flag[i][j+1] = True
        return False
            
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        self.flag = [[True for i in range(self.n)] for j in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    self.flag[i][j] = False
                    if self.dfs(i, j, word[1:]):
                        return True
                    self.flag[i][j] = True
        return False
