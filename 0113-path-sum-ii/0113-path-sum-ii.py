# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def sumPath(root,targetSum,dis):
            nonlocal ans

            if root is None:
                return 

            dis.append(root.val)
            if root.val == targetSum and root.left is None and root.right is None:
                ans.append(dis[:])
            
            targetSum = targetSum - root.val

            sumPath(root.left,targetSum,dis)
            sumPath(root.right,targetSum,dis)

            dis.pop()

        sumPath(root,targetSum,[])
        return ans