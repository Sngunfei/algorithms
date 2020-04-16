
"""
AVL平衡树

左旋 右旋
"""

class AVLnode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLtree:

    def __init__(self):
        raise NotImplementedError("")

    def height(self, node):
        if not node:
            return -1
        return node.height


    def RightRotate(self, node):
        left = node.left
        node.left = left.right
        left.right = node

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        left = max(self.height(left.left), self.height(left.right)) + 1

        return left


    def leftRotate(self, node):
        right = node.right
        node.right = right.left
        right.left = node

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        right = max(self.height(right.left), self.height(right.right)) + 1

        return right


// 左 - 右型，进行左旋，再右旋
static
AvlNode
R_L_Rotate(AvlNode
K3) {
// 先对其孩子进行左旋
K3.lchild = R_Rotate(K3.lchild);
// 再进行右旋
return L_Rotate(K3);
}

// 右 - 左型，先进行右旋，再左旋
static
AvlNode
L_R_Rotate(AvlNode
K3) {
// 先对孩子进行右旋
K3.rchild = L_Rotate(K3.rchild);
// 在左旋
return R_Rotate(K3);
}

// 插入数值操作
static
AvlNode
insert(int
data, AvlNode
T) {
if (T == null) {
T = new AvlNode();
T.data = data;
T.lchild = T.rchild = null;
} else if (data < T.data) {
// 向左孩子递归插入
T.lchild = insert(data, T.lchild);
// 进行调整操作
// 如果左孩子的高度比右孩子大2
if (height(T.lchild) - height(T.rchild) == 2) {
// 左-左型
if (data < T.lchild.data) {
T = R_Rotate(T);
} else {
// 左-右型
T = R_L_Rotate(T);
}
}
} else if (data > T.data) {
T.rchild = insert(data, T.rchild);
// 进行调整
// 右孩子比左孩子高度大2
if (height(T.rchild) - height(T.lchild) == 2)
// 右-右型
if (data > T.rchild.data) {
T = L_Rotate(T);
} else {
T = L_R_Rotate(T);
}
}
// 否则，这个节点已经在书上存在了，我们什么也不做

// 重新计算T的高度
T.height = Math.max(height(T.lchild), height(T.rchild)) + 1;
return T;
}
}