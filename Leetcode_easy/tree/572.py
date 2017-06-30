# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def check(s, t):
            if s is None and t is None:
                return True
            if s is None or t is None:
                return False
            return (s.val == t.val and check(s.left, t.left) and check(s.right, t.right))

        if not s:
            return
        if check(s, t):
            return True
        if self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            return True
        return False




from Leetcode_easy.tree import CreateTree
lst = [1,None ,2]
tree = CreateTree.Create(lst)
CreateTree.depth_tree(tree)
print('^^^^^^^^^^^^^^^^^^^^^')
root = tree._root
s = Solution()