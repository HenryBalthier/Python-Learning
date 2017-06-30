# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        MAX = [-1]
        r = root

        def helper(root):
            if (root.right is None or root.right.val is None) and (root.left is None or root.left.val is None):
                return 1
            if root.left is not None and root.left.val is not None:
                depth_l = helper(root.left)
            else:
                depth_l = 0
            if root.right is not None and root.right.val is not None:
                depth_r = helper(root.right)
            else:
                depth_r = 0
            m = depth_l + depth_r
            if m > MAX[-1]:
                MAX.append(m)
            depth = max(depth_l, depth_r)
            return depth + 1

        n = helper(r) - 1
        if n > MAX[-1]:
            MAX.append(n)
        print(MAX)
        return MAX[-1]


from Leetcode_easy.tree import CreateTree
lst = [1, 2, None, 3, 4, 5, None, 6]
tree = CreateTree.Create(lst)
CreateTree.depth_tree(tree)
print('^^^^^^^^^^^^^^^^^^^^^')
root = tree._root
s = Solution()
print(s.diameterOfBinaryTree(root))