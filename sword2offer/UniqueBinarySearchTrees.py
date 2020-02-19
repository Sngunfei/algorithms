
"""
https://leetcode.com/problems/unique-binary-search-trees/

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
"""

""" 
思路：从1推到n

n=1，ans=1
n=2, ans=2
n=3, ans=5
n=4, 5+5+2+2=14
n=5, 14+14+5+5+2+2
策略：每次选定一个节点作为根时，它的左边和右边各自就有了两个子问题，如果他是i，那么就成了第i和n-1-i个的组合问题
"""


def uniqueBST(n):
    ans = [0] * (n + 1)
    ans[0] = 1
    ans[1] = 1

    def func(k):
        if ans[k] > 0:
            return ans[k]
        cur = 0
        for i in range(0, k):
            # 树可以分为三部分，左子树，根，右子树
            # 数数就行，总共有k个，左边有i个，根有1个，右边就有k-1-i个。
            cur += func(i) * func(1) * func(k-1-i)
        ans[k] = cur
        return ans[k]

    func(n)
    return ans[-1]



