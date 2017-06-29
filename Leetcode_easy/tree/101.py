# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isSametree(root, root)

    def isSametree(self, p, q):
        """
        :param p: TreeNode
        :param q: TreeNode
        :return: bool
        """
        if p == None and q == None:
            return True
        elif p and q:
            return p.val == q.val and self.isSametree(p.left, q.right) and self.isSametree(p.right, q.left)
        else:
            return False
