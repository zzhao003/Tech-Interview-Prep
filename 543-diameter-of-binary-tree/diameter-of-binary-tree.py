# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        def dfs(node):
            if node is None: return 0
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            if leftHeight + rightHeight > diameter[0]:
                diameter[0] = leftHeight + rightHeight
            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return diameter[0]