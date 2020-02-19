# -*- encoding: utf-8 -*-

"""
前中后层序遍历二叉树, 分别用循环和递归实现
"""

def inorderTraversal_loop(root):
    if not root:
        return
    ans = []
    stack = [root]
    while stack:
        cur = stack.pop(-1)
        if cur.left:
            stack.append(cur)
            tmp = cur.left
            cur.left = None
            stack.append(tmp)
        else:
            ans.append(cur.val)
            if cur.right:
                stack.append(cur.right)
    return ans


def inorderTraversal_recursive(root):
    if not root:
        return
    ans = []

    def func(cur):
        if not cur:
            return
        func(cur.left)
        ans.append(cur.val)
        func(cur.right)

    func(root)
    return ans


