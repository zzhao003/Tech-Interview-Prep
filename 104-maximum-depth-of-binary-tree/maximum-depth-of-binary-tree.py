# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root is None: return 0
        # leftHeight = self.maxDepth(root.left)
        # rightHeight = self.maxDepth(root.right)
        # return 1 + max(leftHeight, rightHeight)
        if root is None: return 0

        que = deque([root])
        level = 0
        while que:
            for i in range(len(que)):
                cur = que.popleft()

                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
            level +=1
        return level
