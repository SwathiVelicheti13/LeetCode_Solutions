class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = [[1] * (i + 1) for i in range(numRows)]

        # Populate triangle from row 2 onwards (0-based index)
        for i in range(2, numRows):  # Start from row index 2
            for j in range(1, i):  # Exclude first and last elements
                result[i][j] = result[i-1][j-1] + result[i-1][j]

        return result


        
        