# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(root):
            if root.left:
                dl, flagl = depth(root.left)
            else:
                dl, flagl = (0, True)

            if root.right:
                dr, flagr = depth(root.right)
            else:
                dr, flagr = (0, True)

            if flagr and flagl and abs(dr - dl) <= 1:
                flag = True
            else:
                flag = False
            return max(dr + dl) + 1, flag

        return depth(root)[1]