

"""
回文相关

"""


def countSubstrings(s: str) -> int:
    # 统计回文字符串个数
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
        if i < n - 1 and s[i] == s[i + 1]:
            dp[i][i + 1] = 1

    for length in range(3, n + 1):
        for i in range(0, n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                dp[i][j] = 1

    return sum([sum(row) for row in dp])