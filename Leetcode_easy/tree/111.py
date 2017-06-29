# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min = [99999]
        if not root:
            return 0

        def findmindepth(root, level):
            if root.left is None and root.right is None:
                if level < min[-1]:
                    min.append(level)
                return
            if root.left:
                findmindepth(root.left, level+1)
            if root.right:
                findmindepth(root.right, level+1)

        findmindepth(root, 1)
        return min[-1]

from Leetcode_easy.tree import CreateTree
lst = [1,2,3,4,5]
tree = CreateTree.Create(lst)
root = tree._root
