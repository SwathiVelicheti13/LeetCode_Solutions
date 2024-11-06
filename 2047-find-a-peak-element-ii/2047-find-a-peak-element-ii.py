class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        def maxEle(mat,mid,n,m):
            row = float('-inf')
            ind = -1
            for i in range(n):
                if row < mat[i][mid]:
                    row = mat[i][mid]
                    ind = i
            return ind
            
        n = len(mat)
        m = len(mat[0])
        low= 0 
        high = m-1
        while low<=high:
            mid = (low+high)//2

            row = maxEle(mat, mid, n,m)
            
            if mid-1>=0:
                left = mat[row][mid-1]  
            else:
                left = -1    
            
            if mid+1<m:
                right = mat[row][mid+1] 
            else:
                right = -1

            print(left)
            
            if mat[row][mid] > left and mat[row][mid] > right:
                return [row,mid]  
            elif mat[row][mid] > left:
                low = mid+1
            elif mat[row][mid]> right:
                high = mid-1
        return [-1,-1]