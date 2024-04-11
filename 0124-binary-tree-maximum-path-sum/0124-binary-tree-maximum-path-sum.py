# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxSum = float('-inf')
        
        def helper(root):
            nonlocal maxSum
            
            if not root:
                return 0
            
            leftSum = max(0,helper(root.left))
            rightSum = max(0,helper(root.right))
            
            maxSum = max(maxSum, leftSum + rightSum+root.val)
            
            return max(leftSum,rightSum)+root.val
        
        helper(root)
        return maxSum
        