class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isSafe(num,row,col,board):
            for c in range(len(board[0])):
                if board[row][c] == str(num):
                    return False
            for r in range(len(board)):
                if board[r][col] == str(num):
                    return False
            
            start_row = 3*(row//3)
            start_col = 3*(col//3)

            for i in range(3):
                for j in range(3):
                    if board[start_row+i][start_col+j] == str(num):
                        return False
            return True
        def helper(board):
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col]=='.':
                        for num in range(1,10):
                            if isSafe(num,row,col,board):
                                board[row][col] = str(num)
                                if helper(board):
                                    return True
                                else:
                                    board[row][col] = '.'
                        return False
            return True
                        

        helper(board)
        return board
    