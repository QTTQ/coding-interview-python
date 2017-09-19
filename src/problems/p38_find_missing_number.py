"""
    p38_find_missing_number
    ~~~~~~~~~~~~~~~~~~~~~~

    题目：0~n-1 中缺失的数字

    一个长度为 n-1 的递增排序数组中的所有数字都是唯一的，并且每个
    数字都在范围 0~n-1 之内。在范围 0~n-1 内的 n 个数字中有且只
    有一个数字不在该数组中，请找出这个数字。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def find_missing_number(seq=None):
    """
    首先，这个数组是很有特色的。假设数组长度为 n，则按照递增排序的数组
    下表就等于实际的数字。然而此时是缺失一个整数，也就意味着，在某个位
    置，下标不等于实际的元素。
    这里，问题就转化为查找下标与元素不匹配的节点，并补充缺失值。

    1. 当中间值和下标相等，则在右半边查找；
    2. 当中间值和下标不等，且中间值前一个元素和其下标相等，则当前中间下标就是缺失的值；
    3. 当中间值和下标不等，且中间值前一个元素和其下标不等，则接下来在左半边查找。
    """

    if not seq:
        return None

    left, right = 0, len(seq) - 1
    while left <= right:
        middle = (left + right) >> 1
        if seq[middle] == middle:
            left = middle + 1
        else:
            if seq[middle - 1] == middle - 1 or middle == 0:
                return middle
            else:
                right = middle - 1

    if left == len(seq):
        return left


find_missing_number([1, 2, 3])
