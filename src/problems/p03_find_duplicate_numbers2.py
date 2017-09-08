"""
    p03_find_duplicate_numbers2
    ~~~~~~~~~~~~~~

    问题：不修改数组找出重复的数字

    在一个长度为 n+1 的数组中所有的数字都在 1~n 范围内，所以数组中至少有一个数字是重复的。
    请至少找出数组中任意一个重复的数字，但不能修改输入的数组。

    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def find_dup_numbers(seq):
    """二分法查找，用时间换空间，提高算法空间效率"""
    if seq is None or len(seq) <= 1:
        return None

    start, end = 1, len(seq) - 1

    while start <= end:
        mid = start + (end - start) // 2
        count = count_range(seq, start, mid)

        if end == start:
            if count > 1:
                return start
            else:
                break

        if count > mid - start + 1:
            end = mid
        else:
            start = mid + 1

    return None


def count_range(seq, start, end):
    count = 0
    for x in seq:
        if start <= x <= end:
            count += 1
    return count


if __name__ == '__main__':
    print(find_dup_numbers([0, 1, 2, 2, 3, 4]))
