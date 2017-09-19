"""
    p31_max_sum_of_sub_seq
    ~~~~~~~~~~~~~~~~~~~~~~

    题目：连续子数组的最大和

    输入一个整型数组，数组中有正数也有负数。数组中的一个或连续多个整数构成
    一个子数组。求所有子数组和的最大值。要求时间复杂度为 O(n)。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def max_sum_of_sub_seq(seq=None):
    """
    当累加和小于等于 0 时，重置累加和；否则继续累加
    在累加过程中不断比较最大值。
    """
    if seq is None:
        return None

    if len(seq) == 0:
        return None

    max_sum = 0
    current_sum = 0

    for x in seq:
        if current_sum <= 0:
            current_sum = x
        else:
            current_sum += x

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum
