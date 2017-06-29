class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 广度优先/深度优先遍历二叉树

class BinaryTree:
    def __init__(self):
        self._root = None

    def make_tree(self, node):
        self._root = node

    def insert(self, node):
        # 这里是建立一个完全二叉树
        lst = []
        def insert_node(tree_node, p, node):
            if tree_node.left is None:
                tree_node.left = node
                return
            elif tree_node.right is None:
                tree_node.right = node
                return
            else:
                lst.append(tree_node.left)
                lst.append(tree_node.right)
                insert_node(lst[p + 1], p + 1, node)
        lst.append(self._root)
        insert_node(self._root, 0, node)

def breadth_tree(tree):
    lst = []

    def traverse(node, p):
        if node.left is not None:
            lst.append(node.left)
        if node.right is not None:
            lst.append(node.right)
        if p > (len(lst) -2):
            return
        else:
            traverse(lst[p+1], p+1)

    lst.append(tree._root)
    traverse(tree._root, 0)

    # 遍历结果就存在了lst表里
    for node in lst:
        print(node.val)

def depth_tree(tree):
    lst = []
    lst.append(tree._root)
    while len(lst) > 0:
        node = lst.pop()
        print(node.val)
        if node.right is not None:
            lst.append(node.right)
        if node.left is not None:
            lst.append(node.left)

def Create(lst):
    tree = BinaryTree()
    # 生成完全二叉树
    for (i, j) in enumerate(lst):
        # node = Node(j, None, None)
        node = TreeNode(j)
        if i == 0:
            tree.make_tree(node)
        else:
            tree.insert(node)
    return tree

if __name__ == '__main__':
    lst = [1,2,None,3,None,None,None,4]
    tree = Create(lst)

    # 广度优先遍历
    breadth_tree(tree)

    # 深度优先遍历
    depth_tree(tree)
