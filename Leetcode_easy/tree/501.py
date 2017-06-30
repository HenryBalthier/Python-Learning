# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        dct = {}

        def helper(root):
            if root.val is not None:
                dct[root.val] = 1 + dct.get(root.val, 0)
            if root.left is not None:
                helper(root.left)
            if root.right is not None:
                helper(root.right)

        helper(root)
        d = {}
        for i in dct:
            if d.get(dct[i], None) is None:
                d[dct[i]] = []
            d[dct[i]].append(i)
        m = 0
        for i in d:
            if i > m:
                m = i
        return sorted(d[m])

from Leetcode_easy.tree import CreateTree
lst = [1, None, 2, 2, 1]
tree = CreateTree.Create(lst)
CreateTree.depth_tree(tree)
print('^^^^^^^^^^^^^^^^^^^^^')
root = tree._root
s = Solution()
print(s.findMode(root))