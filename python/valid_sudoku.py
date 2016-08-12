class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def check(line):
            lis = [0 for i in range(9)]
            for ch in line:
                if ch != ".":
                    lis[int(ch) - 1] += 1
            flag = True
            for i in lis:
                if i > 1:
                    flag = False
            return flag
        #check row
        for tmp in board:
            if not check(tmp):
                return False
        #check colunm
        for i in range(9):
            tmp = []
            for j in range(9):
                tmp.append(board[j][i])
            if not check(tmp):
                return False
        #check square
        for i in range(9):
            x = i / 3 * 3
            y = i % 3 * 3
            tmp = []
            tmp += board[x][y:y+3]
            tmp += board[x + 1][y:y+3]
            tmp += board[x + 2][y:y+3]
            if not check(tmp):
                return False
        return True 
