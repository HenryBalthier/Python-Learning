# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """


from Leetcode_easy.tree import CreateTree
lst = [2, 0 , 3, -4, 1]
tree = CreateTree.Create(lst)
CreateTree.breadth_tree(tree)
print('^^^^^^^^^^^^^^^^^^^^^')
root = tree._root
CreateTree.display_b(root)
s = Solution()
print(s.averageOfLevels(root))
