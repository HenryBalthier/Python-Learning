Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        if not t1 and t2:
            res = TreeNode(t2.val)
            res.left = t2.left
            res.right = t2.right
        if t1 and not t2:
            res = TreeNode(t1.val)
            res.left = t1.left
            res.right = t1.right
        if t1 and t2:
            res = TreeNode(t1.val+t2.val)
            res.left = self.mergeTrees(t1.left,t2.left)
            res.right = self.mergeTrees(t1.right,t2.right)
        return res

from Leetcode_easy.tree import CreateTree
lst = [1,None ,2]
tree = CreateTree.Create(lst)
CreateTree.depth_tree(tree)
print('^^^^^^^^^^^^^^^^^^^^^')
root = tree._root
s = Solution()