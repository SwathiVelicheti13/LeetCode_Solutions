# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
    
        def bb(root):
            nonlocal maxSum

            if root is None:
                return 0

            left = max(0,bb(root.left))
            right = max(0,bb(root.right))

            # get determine the max sum
            maxSum = max(maxSum,root.val+left+right)

            # but always consider a path that gives maxsum for exploring larger paths
            return root.val+max(left,right)
            
        bb(root)
        return maxSum
