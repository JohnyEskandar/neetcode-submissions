# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # least common ancestor has to be between p and q
        # start at root
        # if p and q are less than go left
        # if p and q are greater go right
        # if one is greater and one is smaller then its the lca?

        def helper(node):
            val = node.val
            if val > p.val and val > q.val:
                return helper(node.left)
            elif val < p.val and val < q.val:
                return helper(node.right)
            else:
                return node
        
        return helper(root)
