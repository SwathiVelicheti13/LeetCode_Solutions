class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        m = len(matrix[0])

        rowZero = any(matrix[0][j] == 0 for j in range(m))
        colZero = any(matrix[i][0]== 0 for i in range(n))
       

        # marking first rows and columns as zeroes
        for r in range(1,n):
            for c in range(1,m):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # use that markings to mark other rows and columns to zero

        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if rowZero:
            for c in range(m):
                matrix[0][c] = 0
        
        if colZero:
            for r in range(n):
                matrix[r][0] = 0

        


        


        # rows = len(matrix)
        # cols = len(matrix[0])
        # rowSet = set()
        # colSet = set()
        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j] == 0:
        #             rowSet.add(i)
        #             colSet.add(j)
        

        # for i in range(rows):
        #     for j in range(cols):
        #         if i in rowSet or j in colSet:
        #             matrix[i][j] = 0

        # return matrix

    
       