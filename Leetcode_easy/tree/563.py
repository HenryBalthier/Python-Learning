# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        r = root
        res = []
        def helper(root):
            if (root.right is None or root.right.val is None) and (root.left is None or root.left.val is None):
                return root.val
            if (root.left is not None and root.left.val is not None):
                count_l = helper(root.left)
            else:
                count_l = 0
            if (root.right is not None and root.right.val is not None):
                count_r = helper(root.right)
            else:
                count_r = 0

            res.append(abs(count_l - count_r))
            return count_l + count_r + root.val

        _ = helper(r)
        print(res)
        return sum(res)

from Leetcode_easy.tree import CreateTree
lst = [1,None ,2]
tree = CreateTree.Create(lst)
CreateTree.depth_tree(tree)
print('^^^^^^^^^^^^^^^^^^^^^')
root = tree._root
s = Solution()
print(s.findTilt(root))
