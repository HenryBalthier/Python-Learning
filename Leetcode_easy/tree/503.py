# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lst = []
        r = root
        def helper(root):
            if root.val is not None:
                lst.append(root.val)
            if root.left is not None and root.left.val is not None:
                helper(root.left)
            if root.right is not None and root.right.val is not None:
                helper(root.right)

        helper(r)
        lst.sort()
        res = 99999
        for i in range(len(lst) - 1):
            if res > lst[i+1] - lst[i]:
                res = lst[i+1] - lst[i]
        return res

from Leetcode_easy.tree import CreateTree
lst = [1,None ,3, 2]
tree = CreateTree.Create(lst)
CreateTree.depth_tree(tree)
print('^^^^^^^^^^^^^^^^^^^^^')
root = tree._root
s = Solution()
print(s.getMinimumDifference(root))