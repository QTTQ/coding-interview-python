"""
    p37_count_num_in_sorted_array
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    题目：在排序数组中查找数字

    统计一个数字在排序数组中出现的次数。例如：输入排序数组
    [1, 2, 3, 3, 3, 3, 4, 5] 和数字 3，输出 4。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def count_k_in_seq(k, seq=None):
    """思路：
    1. 假设要查找的数字是 k，k 在排序数组中出现的次数可能为 1 次或者多次
    2. 考虑找到第一个 k 和最后一个 k 出现的位置
    3. 两个位置之差就是出现的次数

    查找第一个 k 和最后一个 k 出现位置，可以采用二分法来查找（递归），这样
    整体时间复杂度可以控制到 O(log n)
    """
    if not seq:
        return 0

    first = _get_first_k(seq, 0, len(seq) - 1, k)
    last = _get_last_k(seq, 0, len(seq) - 1, k)

    if first >= 0 and last >= 0:
        return last - first + 1

    return 0


def _get_first_k(seq, start, end, k):
    if start > end:
        return -1

    middle = start + (end - start) // 2

    middle_num = seq[middle]
    if middle_num == k:
        if middle > 0 and seq[middle - 1] != k or middle == 0:
            return middle
        else:
            end = middle - 1
    elif middle_num > k:
        end = middle - 1
    else:
        start = middle + 1

    return _get_first_k(seq, start, end, k)


def _get_last_k(seq, start, end, k):
    if start > end:
        return -1

    middle = start + (end - start) // 2

    middle_num = seq[middle]
    if middle_num == k:
        if middle < len(seq) - 1 and seq[middle + 1] != k or middle == len(seq) - 1:
            return middle
        else:
            start = middle + 1
    elif middle_num < k:
        start = middle + 1
    else:
        end = middle - 1

    return _get_last_k(seq, start, end, k)
