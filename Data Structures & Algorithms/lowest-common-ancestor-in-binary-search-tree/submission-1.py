# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = root
        

        if min(p.val, q.val) <= root.val and max(q.val, p.val) >= root.val:
            return ans
        elif root.val > q.val and root.left:
            print("l")
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.right:
            print("r")
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return ans