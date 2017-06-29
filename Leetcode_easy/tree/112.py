# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        res = []
        if root is None:
            return False

        def count(root, s):
            if root.val:
                s += root.val
            if root.left is None and root.right is None and root:
                res.append(s)
            if root.left:
                count(root.left, s)
            if root.right:
                count(root.right, s)

        count(root, 0)
        print(res)
        return sum in res



from Leetcode_easy.tree import CreateTree
lst = [5,4,8,11,None,13,4,7,2,None,None,None,None,None,1]
tree = CreateTree.Create(lst)
CreateTree.breadth_tree(tree)
CreateTree.depth_tree(tree)
root = tree._root
s = Solution()
s.hasPathSum(root, 22)