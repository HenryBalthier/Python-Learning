# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lst = []
        res = []
        if not root:
            return []
        d = {}
        def Solution(root, p):
            level = lst[p][1]
            if root.left:
                lst.append([root.left, level+1])
            if root.right:
                lst.append([root.right, level+1])
            if p > (len(lst) - 2):
                return
            else:
                Solution(lst[p+1][0], p+1)
        lst.append([root, 0])
        Solution(root, 0)
        for i in lst:
            if i[0].val is not None:
                if not d.get(i[1], None):
                    d[i[1]] = []
                d[i[1]].append(i[0].val)
        print(d)
        for i in d:
            res.append(d[i])
        return res[::-1]


from Leetcode_easy.tree import CreateTree
lst = [1,2,None,3,None,4,None,5]
tree = CreateTree.Create(lst)
root = tree._root
s = Solution()
print(s.levelOrderBottom(root))
