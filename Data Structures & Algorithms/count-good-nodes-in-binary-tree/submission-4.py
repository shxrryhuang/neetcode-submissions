# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, currMax):
            if node is None:
                return 0

            left = dfs(node.left, max(currMax, node.val))
            right = dfs(node.right, max(currMax, node.val))
  
            good = left + right

            if node.val >= currMax:
                good+=1

            return good
            
        return dfs(root, float("-inf"))

