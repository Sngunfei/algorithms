

"""
求二叉树的最大深度

相关问题：判断一棵BST是否是平衡二叉树
"""

def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


def isBalanced(root):
    if not root:
        return True
    if isBalanced(root.left) and isBalanced(root.right):
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        return abs(left_depth - right_depth) <= 1
    return False