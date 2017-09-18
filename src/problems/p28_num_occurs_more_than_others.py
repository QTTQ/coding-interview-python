"""
    p28_num_occurs_more_than_others
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    题目：数组中出现次数超过一半的数字

    数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
    如输入一个长度为 9 的数组 [1, 2, 3, 2, 2, 2, 5, 4, 2]。
    故符合条件的数字是 2。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""
from collections import defaultdict


def find_number_stupid_way(seq=None):
    """
    愚蠢解法的思路：
    1. 遍历整个数组
    2. 遍历过程中将数字出现的次数记录到一个字典中
    3. 当某个数字出现次数超出长度一半时，遍历结束

    分析一下：
    1. 由于需要最多遍历整个数组，最多需要 O(n) 的时间复杂度
    2. 由于需要额外的字典记录次数，则最多需要 O(n/2) 的空间复杂度
    """
    if seq is None:
        return None

    if len(seq) < 1:
        return None

    half_of_length = len(seq) / 2
    records = defaultdict(int)

    for x in seq:
        # 访问字典的时间为 O(1)
        records[x] += 1
        if records[x] > half_of_length:
            return x

    return None


def find_number_smart_way(seq=None):
    """
    这种方法另辟蹊径，同样采用计数的方式，但是不用额外的字典
    来记录。

    思路描述如下：
    1. 设置两个变量 num, count 分别表示扫描中数字及其次数
    2. 由于要寻找的数字出现次数超出数组长度的一半，意味着出现次数比其他数字
       出现次数的总和还要多
    3. 在遍历过程中，每当遇到相同的 num，则 count++；否则 count--
    4. 当 count 减到 0 时，重新设置 num 和 count
    5. 则要寻找的目标就是最后一次重置过 count 的数字
    6. 花费 O(n) 的时间复杂度完成上述扫描；再进行 O(n) 时间复杂度的检查确认。
    """

    if seq is None:
        return None

    if len(seq) == 0:
        return None

    num, count = seq[0], 1
    for x in seq:
        if x == num:
            count += 1
        else:
            count -= 1

        if count == 0:
            num, count = x, 1

    # 进行检查
    return num if _is_more_than_half(seq, num) else None


def _is_more_than_half(seq, target):
    cnt = 0

    for x in seq:
        if target == x:
            cnt += 1

    return cnt * 2 > len(seq)
