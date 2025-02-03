class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        mat = [[0 for _ in range(n)]for _ in range(n)]

        top,left,right,bottom = 0,0,n-1,n-1
        num = 1
        while top<=bottom and left<=right:
            
            # left -> right
            for i in range(left,right+1):
                mat[top][i] = num
                num+=1
            top+=1

            # top-bottom 

            for j in range(top,bottom+1):
                mat[j][right] = num
                num+=1
            right = right-1

            # right->left
            if left<=right:
                for k in range(right,left-1,-1):
                    mat[bottom][k] = num
                    num+=1
                bottom= bottom-1
            
            if top<=bottom:
                for l in range(bottom,top-1,-1):
                    mat[l][left] = num
                    num+=1
                left=left+1

        return mat

        