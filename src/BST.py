# -*- encoding: utf-8 -*-


class Node:
    def __init__(self, val=-1):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self, val):
        newNode = Node(val)
        if not self.root:
            self.root = newNode
        else:
            cur = self.root
            parent = None
            while cur:
                parent = cur
                if val < cur.val:
                    cur = cur.left
                else:
                    cur = cur.right
            if val < parent.val:
                parent.left = newNode
            else:
                parent.right = newNode

            newNode.parent = parent

        self.size += 1

    def _transplant(self, u, v):
        """
        将子树v转移到子树u的位置上
        :param u:
        :param v:
        :return:
        """

        if not u.parent:   # u为root
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def delete(self, node):
        """
        删除一个节点有3种情况：
            1. 如果该节点没有孩子，那么直接删除
            2. 如果该节点有一个孩子，那么孩子顶替该节点
            3. 如果有两个孩子，那么找到该节点的后继节点顶替
        :param node:
        :return:
        """
        if not node:
            return
        if not node.left:
            self._transplant(node, node.right)
        elif not node.right:
            self._transplant(node, node.left)
        else:
            _next = self.minimum(node.right)
            print(node.val, _next.val)
            if _next.parent != node: # 后继节点肯定没有左儿子，同理前驱节点肯定没有右儿子
                self._transplant(_next, _next.right)
                _next.right = node.right
                _next.right.parent = _next
            self._transplant(node, _next)
            _next.left = node.left
            _next.left.parent = _next

        self.size -= 1

    def successor(self, node):
        """
        查询节点node的后继节点
        :param node:
        :return:
        """
        if node.right:
            return self.minimum(node.right)
        p = node.parent
        # 如果该节点一直是右儿子，那么需要往上查，直到找出是左儿子的那个节点，然后把它的父亲节点返回
        # 即是第一个比node节点大的节点
        while p and node == p.right:
            node = p
            p = p.parent
        return p

    def predecessor(self, node):
        """
        查询节点node的前驱节点，和successor对称。
        :param node:
        :return:
        """
        if node.left:
            return self.maximum(node.left)
        p = node.parent
        while p and node == p.left:
            node = p
            p = p.parent
        return p

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if not node:
            return 0

        return 1 + max(self._height(node.left), self._height(node.right))

    def minimum(self, node=None):
        """
        查询某个子树的最小值节点，如果node为空，那么默认从根开始找
        :param node:
        :return: 节点
        """
        cur = self.root if not node else node
        while cur.left:
            cur = cur.left
        return cur

    def maximum(self, node=None):
        """
        和self.minimum类似
        :param node:
        :return:
        """
        cur = self.root if not node else node
        while cur.right:
            cur = cur.right
        return cur

    def find(self, key):
        cur = self.root
        while cur and cur.val != key:
            if cur.val <= key:
                cur = cur.right
            else:
                cur = cur.left
        return cur

    def inorder(self):
        return self._inorder(self.root, [])

    def _inorder(self, node, res):
        if not node:
            return
        self._inorder(node.left, res)
        res.append(node.val)
        self._inorder(node.right, res)
        return res

    def preorder(self):
        return self._preorder(self.root, [])

    def _preorder(self, node, res):
        if not node:
            return
        res.append(node.val)
        self._preorder(node.left, res)
        self._preorder(node.right, res)
        return res

    def postorder(self):
        return self._postorder(self.root, [])

    def _postorder(self, node, res):
        if not node:
            return
        self._postorder(node.left, res)
        self._postorder(node.right, res)
        res.append(node.val)
        return res

    def inorder_stack(self):
        stack = [self.root]
        res = []
        while stack:
            # 沿着左支一路走到底
            while stack[-1].left:
                stack.append(stack[-1].left)

            # 走到底后返回，如果有右节点，就把右节点压到栈里，然后在一路沿左边走到底
            while stack:
                cur = stack.pop()
                res.append(cur)
                if cur.right:
                    stack.append(cur.right)
                    break
        return res

    def preorder_stack(self):
        stack = [self.root]
        res = []

        while stack:
            cur = stack.pop()
            if cur.right:
                res.append(cur.right)
            if cur.left:
                res.append(cur.left)
            res.append(cur.val)
        return res

    def postorder_stack(self):
        stack = [self.root]
        res = []
        prev = None

        while stack:
            while stack[-1].left:
                stack.append(stack[-1].left)
            while stack:
                # 某节点弹出 当且仅当 它没有右儿子或者右儿子已经被弹出且肯定是刚刚被弹出。
                if not stack[-1].right or stack[-1].right == prev:
                    cur = stack.pop()
                    res.append(cur.val)
                    prev = cur
                else:
                    stack.append(stack[-1].right)
                    break
        return res

    def layer_order(self, root=None):
        """
        层序遍历，队列实现
        :return:
        """
        root = self.root if not root else root
        queue = [root]
        res = []

        while queue:
            length = len(queue)
            layer = []
            for _ in range(length):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                layer.append(cur.val)
            res.append(layer)
        return res

    @staticmethod
    def reconstruct_from_preorder_inorder(preorder, inorder):
        """
        根据先序遍历和中序遍历重建二叉树：
            先序遍历中的首节点肯定是根节点，然后在中序遍历中找到根节点的位置，将中序数组一分为二，然后递归创建左右子树。
        :param preorder: list
        :param inorder: list
        :return:
        """
        if not preorder or not inorder:
            return None

        def func(root_idx, _in):
            if not _in:
                return None
            node = Node(preorder[root_idx[0]])
            root_idx[0] += 1
            index = _in.index(node.val)
            # 先建左，再建右
            node.left = func(root_idx, _in[:index])
            if node.left:
                node.left.parent = node
            node.right = func(root_idx, _in[index+1:])
            if node.right:
                node.right.parent = node
            return node

        return func([0], inorder)

    @staticmethod
    def reconstruct_from_postoder_inorder(postorder, inorder):
        """
        根据后序遍历和中序遍历重建二叉树：
            先序遍历中的首节点肯定是根节点，然后在中序遍历中找到根节点的位置，将中序数组一分为二，然后递归创建左右子树。
        :param postorder: list
        :param inorder: list
        :return:
        """
        if not postorder or not inorder:
            return None

        def func(root_idx, _in):
            if not _in:
                return None
            node = Node(postorder[root_idx[0]])
            root_idx[0] -= 1
            index = _in.index(node.val)
            # 先建右，再建左
            node.right = func(root_idx, _in[index + 1:])
            if node.right:
                node.right.parent = node
            node.left = func(root_idx, _in[:index])
            if node.left:
                node.left.parent = node
            return node

        return func([len(postorder)-1], inorder)


    def morris_inorder(self, root):
        """
        morris遍历法，空间复杂度为O（1），在中序遍历中，每个节点的前一个紧邻节点就是它的前序节点
        而且我们知道，前序节点肯定没有右孩子，所以就可以利用这个空指针，让前序节点的右孩子指向当前节点
        这样的话，我们中序遍历，就省去了递归或者栈的空间复杂度。

        总的思路是： 找到前序关系， 大致可以分为几种情形。
        给定一个节点：
        1. 如果这个节点有左孩子，没有右指针，那这个节点的左孩子就是它的前序节点。
        1. 如果这个节点有左孩子，并且有右指针，那么一直往右查，结果就是它的前序节点。
        2. 如果这个节点没有左孩子，并且它是它父亲的右孩子，那么它父亲就是它的前序节点
        3. 如果这个节点没有左孩子，并且它是它父亲的左孩子，那么它没有前序节点，它第一个输出。
        :return:
        """

        # 详情见 sword2offer/world/morris_traversal


        raise NotImplementedError("还没来得及写")


if __name__ == '__main__':
    import random
    tree = BinarySearchTree()
    data = [i for i in range(20)]
    random.shuffle(data)
    print(data)
    for val in data:
        tree.insert(val)
    for i, layer in enumerate(tree.layer_order()):
        print(i, layer)
    print("    ")
    pre = tree.preorder()
    ino = tree.inorder()
    root = BinarySearchTree.reconstruct_from_preorder_inorder(pre, ino)
    for i, layer in enumerate(tree.layer_order(root)):
        print(i, layer)
    print("    ")
    post = tree.postorder()
    root = BinarySearchTree.reconstruct_from_postoder_inorder(post, ino)
    for i, layer in enumerate(tree.layer_order(root)):
        print(i, layer)




