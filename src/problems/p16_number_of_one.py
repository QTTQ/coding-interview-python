"""
    p16_number_of_one
    ~~~~~~~~~~~~~~

    题目：二进制中 1 的个数

    实现一个函数，输入一个整数，输出该整数二进制中 1 的个数。
    如，把 9 表示成二进制是 1001，有 2 位是 1，故返回结果
    位 2。

    这里最重要的思路：把一个整数减去 1 后再和原来的整数做位与
    运算，得到的结果相当于把整数的二进制表示中最右边的 1 变成
    0。
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def number_of_one1(n):
    """常规解法：
    将整数转换位二进制，在转换过程中统计 1 的个数。
    不考虑负整数的情况。
    """
    if n <= 0:
        return 0

    cnt = 0

    while n > 0:
        if n % 2 == 1:
            cnt += 1
        n //= 2

    return cnt


def number_of_one2(n):
    """位运算解法
    在 Python 中，整数位数可以非常大，所以这道题更加适合用 C
    那样的语言求解。
    """
    cnt = 0
    flag = 1

    if n <= 0:
        return 0

    while flag <= n:
        if n & flag:
            cnt += 1

        flag <<= 1

    return cnt


def number_of_one3(n):
    """
    实际是有多少个 1，就会进行多少次操作

    n = 0b1100

    cnt n
    0   0b1100
    1   0b1100 & 0b1011 = 0b1000
    2   0b1000 & 0b0111 = 0b0000
    """
    if n <= 0:
        return 0

    cnt = 0

    while n:
        cnt += 1
        n = n & (n - 1)

    return cnt


#
# 拓展题
#

def is_power_of_two(n):
    """2 的整数次方的值，其中仅有一个 1
    故将其减去 1 后再与自身做与运算，判断
    结果是否 0 即可。
    """
    return (n - 1) & n == 0


def change_bits_to_convert_m_to_n(m, n):
    """
    两个整数 m 和 n，计算需要改变 m 二进制中的多少位才能得到 n。
    """
    # 第一步，做异或运算
    result = m ^ n

    # 统计 1 的个数
    cnt = 0

    while result:
        cnt += 1
        result = result & (result - 1)

    return cnt

if __name__ == '__main__':
    print(number_of_one2(9))
