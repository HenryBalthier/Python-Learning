# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not len(t):
            return '()'
        head = TreeNode(t[0])


def maketree(x):
    if not len(x):
        res = TreeNode(None)
        return res
    head = TreeNode(x[0])
    head.left = maketree(x[1:])
    head.right = maketree(x[2:])
    return head

if __name__ == '__main__':
    s = Solution()
    x = [1,2,3,4]
    t = maketree(x)
    print(s.tree2str(t))