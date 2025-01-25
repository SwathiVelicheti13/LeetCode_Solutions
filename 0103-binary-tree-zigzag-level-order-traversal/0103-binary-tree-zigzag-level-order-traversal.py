# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        if root is None:
            return []
        lr = True
        q = deque([root])
        ans = []
        while q:
            level = []
            n =len(q)

            for i in range(n):
                root = q.popleft()
                level.append(root.val)
                if root.left:
                    q.append(root.left)

                if root.right:
                    q.append(root.right)

            if not lr:
                level.reverse()

            ans.append(level)

            lr = not lr

        return ans



        