# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        res = []
        r = root
        target = sum

        def helper(root, count):
            if root.val is not None:
                count += root.val
                print(count)
                if count == target:
                    res.append(root.val)
            if root.left is not None:
                helper(root.left, count)
            if root.right is not None:
                helper(root.right, count)

        def search(root):
            if root.val is not None:
                helper(root, 0)
            if root.left is not None:
                search(root.left)
            if root.right is not None:
                search(root.right)

        search(r)
        print(res)
        return len(res)

from Leetcode_easy.tree import CreateTree
lst = [10,5,-3,3,2,None,11,3,-2,None,1]
tree = CreateTree.Create(lst)
CreateTree.depth_tree(tree)
print('^^^^^^^^^^^^^^^^^^^^^')
root = tree._root
s = Solution()
sum = 8
print(s.pathSum(root, sum))
