# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root,0)])
        res = {}
        while q:
            root,ind = q.popleft()

            if root is not None:
                try:
                    res[ind].append(root.val)
                except:
                    res[ind] = [root.val]
            else:
                return []
            
            ind+=1
            if root.left:
                q.append((root.left,ind))
            
            if root.right:
                q.append((root.right,ind))
            
        return list(res.values())
        