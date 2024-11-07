class Solution:
    def binaryS(self,nums,target):
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                high = mid -1
            else:
                low = mid+1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            if matrix[i][0]<=target and target<=matrix[i][m-1]:
                return self.binaryS(matrix[i],target)
        return False
        
        