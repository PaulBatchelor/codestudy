# My initial solution
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node, h=0):
            if not node:
                return h
            lh = height(node.left, h + 1)
            rh = height(node.right, h + 1)
            if abs(lh - rh) > 1:
                nonlocal balanced
                balanced = False
            return max(lh, rh)

        balanced = True
        height(root)

        return balanced
