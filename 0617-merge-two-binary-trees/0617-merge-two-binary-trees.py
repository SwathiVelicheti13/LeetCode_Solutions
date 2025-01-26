# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1:
            return root2
        
        if not root2:
            return root1

        temp = root1.val+root2.val
        root = TreeNode(temp)


        root.left = self.mergeTrees(root1.left,root2.left)
        root.right = self.mergeTrees(root1.right,root2.right)

        return root



        #     if root1 is None and root2 is None:
        #         return

        #     if root1 and root2:
        #         temp = root1.val+root2.val
        #         root3 = TreeNode(temp)

        #     elif root1:
        #         root3 = TreeNode(root1)
                

        #     elif root2:
        #         root3 = TreeNode(root2)

        #     root3.left=None
        #     root3.right=None

        #     mergeTree(root1.left,root2.left,root3.left)
        #     mergeTree(root1.right,root2.right,root3.right)
        
        # mergeTree(root1,root2,root3)
        # print(root3)
            
