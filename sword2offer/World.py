
"""
总结一下经典的算法题:

    排序：选择排序，插入排序，冒泡排序，桶排序，快速排序

    二叉树：遍历非递归版本，重建，公共祖先，查找

    链表：合并，翻转，找最后第k个，判断有无环

    字符串：KMP，回文

    动态规划：最长链条，矩阵乘法

    位运算

    栈，队列
"""


def select_sort(nums: list):
    """
    选择排序，复杂度O（N2）
    :param nums: 要排序的数组
    :return: 按升序排列的结果
    """
    n = len(nums)
    for i in range(n):
        cur_min = nums[i]
        cur_pos = i
        for j in range(i+1, n):
            if nums[j] < cur_min:
                cur_min = nums[j]
                cur_pos = j
        nums[i], nums[cur_pos] = nums[cur_pos], nums[i]


def bubble_sort(nums: list):
    """
    冒泡排序，O(N2)
    :param nums:
    :return: 按升序排列的结果
    """
    n = len(nums)
    for idx in range(n):
        for j in range(0, n-idx-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


def insert_sort(nums: list):
    """
    插入排序，当前位置的数，往前挨个查找，直到找到合适位置，插入
    :param nums:
    :return:
    """
    n = len(nums)
    for i in range(1, n):
        cur_num = nums[i]
        j = i - 1
        while j >= 0 and nums[j] >= cur_num:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = cur_num


# ----------------------------------------------------------------------------- #

from Nodes import TreeNode

def inorder_traversal_loop(root: TreeNode) -> list:
    """
    中序遍历的非递归版本，一直压左边，左边压完了后打印自身，然后再压右边
    :param root:
    :return:
    """
    if not root:
        return []
    res = []
    stack = [root]
    while stack:
        while stack[-1].left:
            stack.append(stack[-1].left)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
                break
    return res


def postorder_traversal_loop(root: TreeNode) -> list:
    if not root:
        return []
    res = []
    stack = [root]
    prev = None
    while stack:
        while stack[-1].left:
            stack.append(stack[-1].left)
        while stack and stack[-1].right == prev:
            cur = stack.pop()
            res.append(cur.val)
            prev = cur
        if stack and stack[-1].right:
            stack.append(stack[-1].right)


def siftdown(nums, cur_pos):
    n = len(nums)
    child = 1 + (cur_pos << 1)
    val = nums[cur_pos]
    while child < n:
        right = child + 1
        if right < n and nums[right] <= nums[child]:
            child = right
        if nums[child] < val:
            nums[cur_pos], nums[child] = nums[child], nums[cur_pos]
            cur_pos = child
            child = 1 + (cur_pos << 1)
            continue
        break


def heapify(nums: list):
    n = len(nums)
    for i in reversed(range(n//2)):
        siftdown(nums, i)


def heappop(nums: list):
    last = nums.pop()
    if nums:
        val, nums[0] = nums[0], last
        siftdown(nums, 0)
        return val
    return last


def heappush(nums: list, val: int):
    nums.append(val)
    cur = len(nums) - 1
    while cur > 0:
        parent_pos = (cur - 1) >> 1
        if nums[cur] < nums[parent_pos]:
            nums[cur], nums[parent_pos] = nums[parent_pos], nums[cur]
            cur = parent_pos
            continue
        break


def insert_loop(root: TreeNode, val) -> TreeNode:
    if not root:
        return TreeNode(val)
    cur = root
    parent = None
    while cur:
        parent = cur
        if cur.val <= val:
            cur = cur.right
        else:
            cur = cur.left
    if parent.val <= val:
        parent.right = TreeNode(val)
    else:
        parent.left = TreeNode(val)
    return root


def insert_recur(root: TreeNode, val) -> TreeNode:
    if not root:
        return TreeNode(val)
    if root.val <= val:
        root.right = insert_recur(root.right, val)
    else:
        root.left = insert_recur(root.left, val)
    return root

def find_loop(root: TreeNode, key):
    if not root:
        return None
    cur = root
    while cur and cur.val != key:
        if cur.val <= key:
            cur = cur.right
        else:
            cur = cur.left
    return cur


def delete_loop(root: TreeNode, key):
    if not root:
        return
    cur = root
    parent = None
    while cur:
        if cur.val == key:
            break
        parent = cur
        if cur.val < key:
            cur = cur.right
        elif cur.val > key:
            cur = cur.right
    # 未找到该节点
    if not cur:
        return

    if cur.left is None:
        if parent.left == cur:
            parent.left = cur.right
        else:
            parent.right = cur.right
    elif cur.right is None:
        if parent.left == cur:
            parent.left = cur.left
        else:
            parent.right = cur.left
    else:
        # 左右子树都不为空，找后继节点
        prev = cur
        tmp = cur.right
        while tmp.left:
            prev = tmp
            tmp = tmp.left
        cur.val = tmp.val
        prev.left = None
    return root


def morris_inorder_traversal(root: TreeNode):
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
    if not root:
        return
    res = [] # 中序遍历结果
    cur = root

    def getPrev(node):
        # 查找前序节点
        tmp = node.left
        while tmp.right and tmp.right != node:
            tmp = tmp.right
        return tmp

    while cur:
        if not cur.left:
            res.append(cur.val)
            cur = cur.right
        else:
            prev = getPrev(cur) # 拿到前序节点

            if not prev.right:
                prev.right = cur
                cur = cur.left
            else:
                prev.right = None
                res.append(cur.val)
                cur = cur.right
    return res


def morris_preorder_traversal(root: TreeNode):
    """
    和上面的方法类似，只在于输出的时候放在哪一部分

    中序遍历的时候是要求第二次回到curNode时才输出
    而前序遍历是第一次回到curNode的时候就输出，也就是先于自己的前序节点。
    :return:
    """
    if not root:
        return
    res = [] # 中序遍历结果
    cur = root

    while cur:
        if not cur.left:
            res.append(cur.val) # 这一块没变
            cur = cur.right
        else:
            # 同样找前序节点
            prev = cur.left
            while prev.right and prev.right != cur:
                prev = prev.right

            if not prev.right:
                res.append(cur.val)
                prev.right = cur
                cur = cur.left
            else:
                prev.right = None
                cur = cur.right

    return res



if __name__ == '__main__':
    import random
    import heapq
    print(10 % 10)

