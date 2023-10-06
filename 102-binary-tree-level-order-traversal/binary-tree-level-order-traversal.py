# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # q = deque([root])
        # res = []
        # while q:
        #     temp = []
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node:
        #             q.append(node.left)
        #             q.append(node.right)
        #             temp.append(node.val)
        #     if temp:
        #         res.append(temp)
        # return res
        def dfs(node,level,hashmap):
            if node == None:
                return
            if level not in hashmap:
                hashmap[level] = []
            hashmap[level].append(node.val)

            dfs(node.left, level+1, hashmap)
            dfs(node.right, level+1, hashmap)

        hashmap = {}
        dfs(root,0, hashmap)
        return hashmap.values()
    	# def dfs(node,level,hashmap):
      	#     if node == None:
        #         return
        #     if level not in hashmap:
        #   	    hashmap[level] = []
      
        #     hashmap[level].append(node.val)
          
        #     dfs(node.left, level+1,hashmap)
        #     dfs(node.right, level+1,hashmap)
     
        # hashmap = {}
        # dfs(root,0,hashmap)
      
        # return list(hashmap.values())