# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = []
        r = root

        def helper(root, isleft):
            if (root.right is None or root.right.val is None)and (root.left is None or root.left.val is None):
                if root.val is not None and isleft:
                    res.append(root.val)
            if root.left is not None:
                if root.left.val is not None:
                    helper(root.left, 1)
            if root.right is not None:
                if root.right.val is not None:
                    helper(root.right, 0)

        helper(r, 0)
        print(res)
        return sum(res)

from Leetcode_easy.tree import CreateTree
lst = [3,9,20,None,None,15,17]
tree = CreateTree.Create(lst)
CreateTree.depth_tree(tree)
print('^^^^^^^^^^^^^^^^^^^^^')
root = tree._root
s = Solution()
print(s.sumOfLeftLeaves(root))