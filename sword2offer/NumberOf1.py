
"""
给定一个正数n，统计从1到n所有数字中，十进制，1出现的次数
比如13：
1，10,11,12,13
"""

def numberOf1(n: int) -> int:
    """
    一位一位的来
    21345，先考虑万位，再考虑千位
    :param n:
    :return:
    """
    nums = []
    while n:
        nums = [n % 10] + nums
        n //= 10

    cnt = 0
    for idx, num in enumerate(nums):
        if num > 1:
            return 0


