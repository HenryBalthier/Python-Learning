# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or p is None or q is None:
            return None
        res1 = []
        res2 = []
        target = root
        res1.append(target)
        res2.append(target)
        while target is not p:
            if target.val < p.val:
                target = target.right
            elif target.val > p.val:
                target = target.left
            res1.append(target)
        target = root
        while target is not q:
            if target.val < q.val:
                target = target.right
            elif target.val > q.val:
                target = target.left
            res2.append(target)
        for i in res1:
            print(i.val)
        for i in res2:
            print(i.val)
        lenth = min(len(res1), len(res2))
        for i in range(lenth):
            if res1[i] is not res2[i]:
                return res1[i-1]
        return res1[lenth-1]




from Leetcode_easy.tree import CreateTree
lst = [6,2,8,0,4,7,9,None,None,3,5]
tree = CreateTree.Create(lst)
CreateTree.depth_tree(tree)
print('^^^^^^^^^^^^^^^^^^^^^')
root = tree._root
s = Solution()
p = root
q = root
print(s.lowestCommonAncestor(root, p, q).val)