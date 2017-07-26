# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        def generate_greater_tree(node):
            if not node: return None
            right = generate_greater_tree(node.right)
            self.sum += node.val
            new_node = TreeNode(self.sum)
            new_node.right = right
            new_node.left = generate_greater_tree(node.left)
            return new_node

        self.sum = 0
        return generate_greater_tree(root)


from Leetcode_easy.tree import CreateTree
lst = [2, 0 , 3, -4, 1]
tree = CreateTree.Create(lst)
CreateTree.depth_tree(tree)
print('^^^^^^^^^^^^^^^^^^^^^')
root = tree._root
s = Solution()
CreateTree.display(s.convertBST(root))
