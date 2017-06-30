# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        res = []
        target = root

        def helper(root, s):
            if root is not target:
                s = s + '->' + str(root.val)
            if root.val is None:
                return
            if root.left is None and root.right is None:
                res.append(s)
                return
            if root.left is not None:
                helper(root.left, s)
            if root.right is not None:
                helper(root.right, s)

        helper(target, str(target.val))
        return res

from Leetcode_easy.tree import CreateTree
lst = []
tree = CreateTree.Create(lst)
CreateTree.depth_tree(tree)
print('^^^^^^^^^^^^^^^^^^^^^')
root = tree._root
s = Solution()
print(s.binaryTreePaths(root))