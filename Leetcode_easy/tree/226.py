# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        r = TreeNode(root.val)
        def Solution(root, r):
            if root.left is None and root.right is None:
                return
            if root.left:
                r.right = TreeNode(root.left.val)
                Solution(root.left, r.right)
            if root.right:
                r.left = TreeNode(root.right.val)
                Solution(root.right, r.left)
        Solution(root, r)
        return r

from Leetcode_easy.tree import CreateTree
lst = [1,2,3,4,5]
tree = CreateTree.Create(lst)
#CreateTree.breadth_tree(tree)
CreateTree.depth_tree(tree)
root = tree._root
s = Solution()
r2 = s.invertTree(root)
t2 = CreateTree.BinaryTree()
t2.make_tree(r2)
CreateTree.depth_tree(t2)