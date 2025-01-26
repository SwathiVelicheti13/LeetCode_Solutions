# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        sum1 = 0

        def sumNum(root,dis):
            nonlocal sum1
            if root is None:
                return 0
            
            dis.append(root.val)
            if root.left is None and root.right is None:
                str1 = ''.join(map(str, dis))
                sum1+=int(str1)

            sumNum(root.left,dis)
            sumNum(root.right,dis)

            dis.pop()

        sumNum(root,[])
        return sum1

            
        