class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m = len(board)
        if m == 0:
            return 0
        n = len(board[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    if (i == 0 or (i > 0 and board[i - 1][j] == '.')) and (j == 0 or (j > 0 and board[i][j - 1] == '.')):
                        res += 1
        return res
