class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.' for _ in range(n)] for _ in range(n)]

        ans = []

        def isSafe(row,col,board):
            duprow = row
            dupcol = col

            while 0<=col<len(board[0]):
                if board[row][col] == 'Q':
                    return False
                col = col-1
            
            row = duprow
            col = dupcol

            while 0<=row<len(board) and 0<=col<len(board):
                if board[row][col] == 'Q':
                    return False
                row = row-1
                col = col-1
            
            row = duprow
            col = dupcol
            
            while 0<=row<len(board) and 0<=col<len(board):
                if board[row][col] == 'Q':
                    return False
                row+=1
                col = col-1
            
            return True


        def SolveN(col):
            if col == n:
                list1 = []
                for x in range(len(board)):
                    list1.append(''.join(board[x]))
                ans.append(list1)
            

            for row in range(len(board)):
                if 0<=col<len(board) and isSafe(row,col,board):
                    board[row][col] = 'Q'
                    SolveN(col+1)
                    board[row][col] = '.'

        SolveN(0)
        return ans

        
        