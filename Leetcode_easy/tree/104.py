# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = dl = dr = 0
        if root == None:
            return depth
        else:
            if root.left:
                dl = self.maxDepth(root.left)
            if root.right:
                dr = self.maxDepth(root.right)
            depth += max(dr, dl)
            return depth + 1