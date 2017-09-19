"""
    p39_find_num_matches_index
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    题目：数组中数值和下标相等的元素

    假设一个单调递增的数组里的每个元素都是整数且是唯一的，编写一个函数，
    找出数组中任意一个数值等于其下标的元素。如，在数组 [-3, -1, 1, 3, 5]
    中，数字 3 和它的下标相等。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def find_num_matches_its_index(seq=None):
    """
    采用二分查找法：
    1. 如果中间值等于下标，则找到
    2. 如果中间值大于下标，则向左找
    3. 如果中间值小于下标，则向右找
    """
    if not seq:
        return None

    length = len(seq)
    left, right = 0, length - 1

    while left <= right:
        middle = (left + right) >> 1

        middle_value = seq[middle]

        if middle_value == middle:
            return middle_value
        elif middle_value > middle:
            right = middle - 1
        else:
            left = middle + 1
