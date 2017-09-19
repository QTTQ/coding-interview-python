"""
    p32_num_of_one
    ~~~~~~~~~~~~~~

    题目：1~n 整数中 1 出现的次数

    输入一个整数 n，求 1~n 这 n 个整数的十进制表示中 1 出现的
    次数。如输入 12，1~12 这些整数中包含 1 的数字有 1，10 和
    11, 12，共出现了 5 次。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def count_total_ones_stupid_way(n):
    """
    先看看最笨的解法：
    从 1 到 n 遍历，遍历过程中拆解 x，统计每个 x 的 1 的个数
    """
    if n < 1:
        return 0

    def count(x):
        s = 0
        while x > 0:
            if x % 10 == 1:
                s += 1
            x //= 10

        return s

    cnt = 0
    while n >= 1:
        cnt += count(n)
        n -= 1

    return cnt


if __name__ == '__main__':
    print(count_total_ones_stupid_way(88))
