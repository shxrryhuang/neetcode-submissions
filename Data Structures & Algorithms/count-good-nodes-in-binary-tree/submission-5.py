# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0 
        
        queue = deque([(root,float("-inf"))])
        good = 0 
        while queue:
            node, currMax = queue.popleft()

            if node.val >= currMax:
                good+=1
            
            newMax = max(currMax, node.val)

            if node.left:
                queue.append((node.left,newMax))

            if node.right:
                queue.append((node.right,newMax))

        return good