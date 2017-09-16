"""
    p15_cut_rope
    ~~~~~~~~~~~~~~

    问题：剪绳子

    给你一个长为 n 的绳子，要求剪成 m 段，每段绳子的长度记为 k[0], k[1], ..., k[m]，
    问 k[0] * k[1] * ... * k[m] 的最大乘积是多少？如绳子长度是 8，则剪成 2, 3, 3 三
    段，可以得到乘积最大为 18。

    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def max_product_after_cutting1(n):
    """动态规划解法
    应用动态规划求解的特点：
    1. 需要求解最优值
    2. 大问题可以划分为小问题，每个小问题都有最优值
    3. 小问题之间有重叠
    4. 从上往下分析问题，从下往上求解问题，小问题最优解一般放在
       一个数组中，最后逐步组合得到大问题的最优解

    分析：假设函数 f(n) 为把长度为 n 的绳子剪成若干段后各段乘积的
    最大值。在剪第一刀时，会有 n-1 种可能的选择，则可以得到 f(n) 为：
    `f(n) = max(f(i) * f(n-i))`，其中 i 在 0 到 n 之间。

    时间复杂度：O(n^2)
    空间复杂度：O(n)
    """
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    products = [None for _ in range(n + 1)]
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3
    max_product = 0

    for i in range(4, n + 1):
        # 由于 1, 3 和 3, 1 是一样的，所以只需要
        # 计算前一半即可
        for j in range(1, i // 2 + 1):
            product = products[j] * products[i - j]
            if max_product < product:
                max_product = product

            products[i] = max_product

    return products[n]


def max_product_after_cutting2(n):
    """贪婪解法

    当 n >=5 时，可以证明 3(n-3) > n 且 2(n-2) > n，
    且 3(n-2) > 2(n-2)。当 n = 4 时，此时应该切成 2 * 2
    保证乘积最大。所以，总体策略是，首先尽可能将将绳子剪成长度
    为 3，当剩余绳子长度为 2 时，剪成长度 2 的两段。

    时间复杂度：O(1)
    空间复杂度：O(1)
    """

    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    # 首先尽可能剪成长度为 3 的段，记录最多可以剪成多少段
    times_of_three = n // 3

    # 当剩余长度为 4 时，则不能剪成长度为 3 的绳子段了
    # 此时，切分成 2 * 2 的段
    if n - times_of_three * 3 == 1:
        times_of_three -= 1

    times_of_two = (n - times_of_three * 3) // 2
    return (3 ** times_of_three) * (2 ** times_of_two)
